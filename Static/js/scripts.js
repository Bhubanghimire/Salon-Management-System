var yearMin = 1950,
  yearMax = 2022,
  selectYear = document.getElementById("yearDatalist");

for (var i = yearMin; i <= yearMax; i++) {
  var opt = document.createElement("option");
  opt.value = i;
  opt.innerHTML = i;
  selectYear.appendChild(opt);
}

var month = [
  "January",
  "February",
  "March",
  "April",
  "May",
  "June",
  "July",
  "August",
  "September",
  "October",
  "November",
  "December",
],
  selectMonth = document.getElementById("monthDatalist");

for(var i = 0; i < month.length; i++) {
  var opt = document.createElement("option");
  opt.value = month[i];
  opt.innerHTML = month[i];
selectMonth.appendChild(opt);
}

var dateMin = 1,
  dateMax = 32,
  selectDate = document.getElementById("dateDatalist");

for (var i = dateMin; i <= dateMax; i++) {
    var opt = document.createElement("option");
    opt.value = i;
    opt.innerHTML = i;
    selectDate.appendChild(opt);
}