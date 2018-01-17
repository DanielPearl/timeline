function display_event1() {
  var event1 = document.getElementById("event1")
  var event2 = document.getElementById("event2")
  var result = document.getElementById("result")
  var y1 = document.getElementById("year1")
  var y2 = document.getElementById("year2")
  var year1 = parseInt(event1.value)
  var year2 = parseInt(event2.value)

  if (year1 < year2){
    result.innerHTML = "Correct!";
  } else {
    result.innerHTML = "Wrong!";
  }
  y1.textContent = year1
  y2.textContent = year2

}

function display_event2() {
  var event1 = document.getElementById("event1")
  var event2 = document.getElementById("event2")
  var result = document.getElementById("result")
  var y1 = document.getElementById("year1")
  var y2 = document.getElementById("year2")
  year1 = parseInt(event1.value)
  year2 = parseInt(event2.value)

  if (year1 > year2){
    result.innerHTML = "Correct!";
  } else {
    result.innerHTML = "Wrong!";
  }
  y1.textContent = year1
  y2.textContent = year2
}
