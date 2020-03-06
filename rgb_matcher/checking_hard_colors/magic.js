var colours = [
  [233,2,206],
[247,235,116],
[248,243,201],
[237,188,158],
[151,211,211],
[249,237,223],
[229,160,127],
[210,141,172],
[197,113,149],
[255,121,120],
[165,0,34],
[253,177,39],
[234,200,217],
[227,211,222],
[154,0,255],
[125,163,199],
[105,144,185],
[97,144,154],
[255,102,0],
[177,203,226],
[205,204,0],
[128,154,191],
[155,175,212],
[201,203,228],
[180,165,204],
[144,145,193],
[204,253,48],
[254,204,203],
[133,117,164],
[216,215,211],
[94,86,73],
[179,180,175],
[139,141,136],
[125,126,121],
[254,102,203],
[163,131,74],
[55,251,250],
[245,220,66],
[248,203,58],
[0,128,1],
[81,108,77],
[224,146,61],
[159,66,87],
[0,0,0],
[130,114,80],
[127,127,75],
[163,172,79],
[212,215,72],
[136,187,86],
[127,128,0],
[60,94,106],
[65,150,119],
[254,0,0],
[92,144,80],
[53,128,134],
[255,255,255],
[0,0,254],
[255,255,0],
[0,255,1],
[94,88,136],
[82,68,94],
[63,71,82],
[65,65,65]
];


function move_comas(rgb) {
  return rgb[0].toString()+"-"+rgb[1].toString()+"-"+rgb[2].toString()
}

function change_color(rgb,level) {
  var palette2 = $('ul#2');
  var new_rgb = ''
  $.ajax({
    type: "GET",
    url: "http://localhost:5002/changecolor/"+move_comas(rgb)+"/"+level,
    data: { param: new_rgb}
  }).done(function( o ) {
    new_rgb = o.data.join(',')
    console.log(new_rgb)
    palette2.append($('<li> '+new_rgb+'</li>').css('background-color', 'rgb('+new_rgb +')'));
  });
}

function render_colors(level=0.5) {
  for (var i = 0; i < colours.length; i++)
  { change_color(colours[i],level)}
}

$(document).ready(function() {


    var $select = $(".0-100");
    for (i=0;i<=100;i+=10){
        if(i==50){
          $select.append($('<option selected></option>').val(i/100).html(i.toString()+"%"))

        }
        $select.append($('<option></option>').val(i/100).html(i.toString()+"%"))
    }


  var palette = $('ul#1');
  for (var i = 0; i < colours.length; i++)
  {
      palette.append($('<li>' +colours[i]+'</li>').css('background-color', 'rgb(' + colours[i].join(',') + ')'));
  }
  render_colors()
});

$(document).ready(function() {
  $('select').change( function () {
    level = $('.0-100 :selected').val()
    var palette2 = $('ul#2');
    palette2.empty()
    render_colors(level)
    
  })
});