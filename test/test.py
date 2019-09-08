
import datetime
import pytz

// date = [18, 8, 24, 13, 45];
var newdate = new Date(Date.UTC(2018, 08, 24, 15, 00, 00));
console.log(newdate)
console.log(newdate.toUTCString());
