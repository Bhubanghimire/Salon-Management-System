now = new Date();
nowYear = now.getFullYear();

// Year selector in date of birth
var yearMin = nowYear - 70,
  yearMax = nowYear,
  selectYear = document.getElementById("yearDatalist");

if (selectYear) {
  for (var i = yearMax; i >= yearMin; i--) {
    var opt = document.createElement("option");
    opt.value = i;
    opt.innerHTML = i;
    selectYear.appendChild(opt);
  }
}

// Month selector in date of birth and appointments
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

if (selectMonth) {
  for (var i = 0; i < month.length; i++) {
    var opt = document.createElement("option");
    opt.value = month[i];
    opt.innerHTML = month[i];
    selectMonth.appendChild(opt);
  }
}

// Day selector in date of birth
var dateMin = 1,
  dateMax = 32,
  selectDate = document.getElementById("dateDatalist");

if (selectDate) {
  for (var i = dateMin; i <= dateMax; i++) {
    var opt = document.createElement("option");
    opt.value = i;
    opt.innerHTML = i;
    selectDate.appendChild(opt);
  }
}

// Year selector in appointments
var yearMin = nowYear - 5,
  yearMax = nowYear + 2,
  selectAppointmetYear = document.getElementById("appointmentYearDatalist");
appointmentYear = document.getElementById("appointmentYear");
appointmentMonth = document.getElementById("appointmentMonth");
appointmentDate = document.getElementById("appointmentDate");

if (selectAppointmetYear) {
  for (var i = yearMax; i >= yearMin; i--) {
    var opt = document.createElement("option");
    opt.value = i;
    opt.innerHTML = i;
    selectAppointmetYear.appendChild(opt);
  }
  if (appointmentYear && appointmentMonth && appointmentDate) {
    appointmentYear.value = nowYear;
    appointmentMonth.value = month[now.getMonth()];
    appointmentDate.value = now.getDate();
  }
}

// Time to select in time selector

var currentTime = now.toISOString().substring(11,16);
document.getElementById('timeSelect').value = currentTime;
