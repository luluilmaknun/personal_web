$(document).ready(function(){
  $.ajax({
    type: "GET",
    url: "get_cal/",
    dataType: 'json',
    success: function(response){
      console.log(response);
      column = 0;
      row = 0;
      text = "<tr id= " + row + ">";
      for(i = 0; i < response[0]; i++){
        text += "<td id= " + column + " height='100' " + ">  </td>";
        column++;

      }
      text += "{% for day in days %}"
      for(i = 1; i < response.length; i++){
        if(column > 6 ){
          column = 0;
          row++;
          text += "</tr><tr id= " + row + ">";
        }
        text += "<td id= " + column + " height='100' " + "> " + i + " </td>";
        column++;
      }
      text += "{% endfor %}</tr>";
      $("tbody").append(text);
    }
  });
})
