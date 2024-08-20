function changeClassService(){
  var element1 = document.querySelector("#content-item-1");
  var element2 = document.querySelector("#content-item-2");
  var element3 = document.querySelector("#content-item-3");

  element1.classList.replace("lower-item", "top-item");
  element2.classList.replace("top-item", "lower-item");
  element3.classList.replace("top-item", "lower-item");
}

function changeClassMission() {
  var element1 = document.querySelector("#content-item-1");
  var element2 = document.querySelector("#content-item-2");
  var element3 = document.querySelector("#content-item-3");

  element1.classList.replace("top-item", "lower-item");
  element2.classList.replace("lower-item", "top-item");
  element3.classList.replace("top-item", "lower-item");
}

function changeClassDebt() {
  var element1 = document.querySelector("#content-item-1");
  var element2 = document.querySelector("#content-item-2");
  var element3 = document.querySelector("#content-item-3");

  element1.classList.replace("top-item", "lower-item");
  element2.classList.replace("top-item", "lower-item");
  element3.classList.replace("lower-item", "top-item");
}