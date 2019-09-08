$(document).ready(function() {
  $.getJSON("/js/data.json", function(json){
    console.log(json);
    list = ['"Biomass"', '"Nuclear"', '"Solar"', '"Fossil Gas"', '"Fossil Hard coal"', '"Hydro"', '"Wind"'];
    for (var i in list){
      for (var Key in json) {
        if (Key == list[i]){
          var jsonStr = JSON.stringify(json[Key]);
          document.getElementById(Key).innerHTML = jsonStr;
        }
      }
    }
  });
});
