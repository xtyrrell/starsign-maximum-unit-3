// find all `img` that are inside `a`
// attach a click listener that logs that img src
function attachEventRecordingClickListeners() {
  const clickable = [...document.querySelectorAll("a img")];

  clickable.forEach((clickable) => {
    clickable.addEventListener("click", (event) => {
      const eventToLog = {
        eventType: event.type,
        contentType: "image",
        content: event.target.src,
        datetime: new Date(),
      };
      recordEvent(eventToLog);
    });
  });
}

attachEventRecordingClickListeners();

// ==========

function recordEvent(event) {
  const events = JSON.parse(localStorage.getItem("events") ?? "[]");

  events.push(event);

  localStorage.setItem("events", JSON.stringify(events));
}

// ==========

/**
 * Resets localStorage `events` when you go to the homepage.
 */
window.addEventListener("pageshow", (event) => {
  if (document.location.pathname === "/" || document.location.pathname === "") {
    console.log("YOU ARE ON THE START PAGE! Clearing events");
    localStorage.setItem("events", JSON.stringify([]));
  }
});

/**
 * Downloads the event log when you go to a page containing `download` in the path.
 */
window.addEventListener("pageshow", (event) => {
  if (document.location.pathname.includes("download")) {
    console.log("YOU ARE ON THE DOWNLOAD PAGE! Downloading events");
    const filename = "events.json";
    const text = localStorage.getItem("events");
    download(filename, text);
  }
});

// Make download buttons download
[...document.querySelectorAll("button.download-events")].forEach(
  (clickable) => {
    clickable.addEventListener("click", () => {
      const filename = "events.json";
      const text = localStorage.getItem("events");
      download(filename, text);
    });
  }
);

// Make next buttons work properly
[...document.querySelectorAll("a.next")].forEach((clickable) => {
  clickable.addEventListener("click", (event) => {
    event.preventDefault();

    goToNextPage();
  });
});

// =================
// === utilities ===
// =================

function goToNextPage() {
  const currentPageStr = window.location.pathname
    .replace("/", "")
    .split(".")[0];
  const currentPage = parseInt(currentPageStr);
  window.location = currentPage + 1 + ".html";
}

function download(filename, text) {
  var element = document.createElement("a");
  element.setAttribute(
    "href",
    "data:text/plain;charset=utf-8," + encodeURIComponent(text)
  );
  element.setAttribute("download", filename);

  element.style.display = "none";
  document.body.appendChild(element);

  element.click();

  document.body.removeChild(element);
}
