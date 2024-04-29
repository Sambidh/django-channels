console.log("Hello world");

const dashboardSlug = document
  .getElementById("dashboard-slug")
  .textContent.trim();
const user = document.getElementById("user").textContent.trim();
const submitBtn = document.getElementById("submit-btn");
const dataInput = document.getElementById("data-input");
const dataBox = document.getElementById("data-box");

const socket = new WebSocket(
  `ws://${window.location.host}/ws/${dashboardSlug}/`
);
console.log(socket);

socket.onmessage = function (e) {
  const { sender, message } = JSON.parse(e.data);

  dataBox.innerHTML += `<p>${sender}: ${message}</p>`;
};

submitBtn.addEventListener("click", () => {
  const dataValue = dataInput.value;
  socket.send(
    JSON.stringify({
      message: dataValue,
      sender: user,
    })
  );
});
