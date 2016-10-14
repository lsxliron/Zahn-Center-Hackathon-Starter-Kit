$(document).ready(function(){
  $("#submit_button").on('click', function(){
    var ticker = $("#ticker").val()
    $.ajax({
      url: "http://0.0.0.0:5500/answer",
      contentType: "application/json",
      type:"post",
      data:JSON.stringify({"ticker":ticker, store:false}),
      success: function(data){
        var answer = "The price of " + data.name + ' stock is ' + data.price
        $("#answer").text(answer)
      }
    })
  })

  setInterval(function(){
    $.ajax({
      url: "http://0.0.0.0:5500/answer",
      contentType: "application/json",
      type:"post",
      data:JSON.stringify({ticker: "IBM", store: true}),
      success: function(data){
        console.log(data)
        var answer = "The price of " + data.name + ' stock is ' + data.price
        console.log(answer)
        $("#autoUpdate").text(answer)
      }
    })
  }, 5000)
})