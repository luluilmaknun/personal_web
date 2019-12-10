$(document).ready(function(){
  $.ajax({
    type: "GET",
    url: "get_cal/",
    dataType: 'json',
    success: function(response){
      column = 0;
      row = 0;
      text = "<tr id= " + row + ">";
      for(i = 0; i < response[0]; i++){
        text += "<td id= " + column + " height='100' " + ">  </td>";
        column++;

      }

      for(i = 1; i < response.length + 1; i++){
        if(column > 6 ){
          column = 0;
          row++;
          text += "</tr><tr id= " + row + ">";
        }
        text += "<td id= " + column + " height='100' " + "> " + i;
        text+= "</td>";
        column++;
      }
      text += "</tr>";
      $("tbody").append(text);
    }
  });
})
