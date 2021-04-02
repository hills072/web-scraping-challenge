var content;
var newsItems = [];
var imgprefix = 'https://mars.nasa.gov';
var itemdisplay = 15;
var dropyears = [];
var categories = [];

$(document).ready(function () {

	getData();

});

var dMinus = new Date();
dMinus.setMonth(dMinus.getMonth() - 1);
var dateArray=[];
//var ranDate = new Date(randomDate(new Date(), new Date())).toLocaleDateString('en-US', {  month: 'long',day: 'numeric', year: 'numeric' });
var ranDate = new Date(randomDate(new Date(), new Date()));
dateArray.push(ranDate);
for (x=0;x<13;x++)
{
 //   var newDate= new Date(randomDate(dMinus, new Date())).toLocaleDateString('en-US', {  month: 'long',day: 'numeric', year: 'numeric' });
    var newDate= new Date(randomDate(dMinus, new Date()));
	dateArray.push(newDate);
}
dateArray.push(new Date());
dateArray.sort(function(a,b){
  return new Date(a) - new Date(b)
})
//dateArray.sort();
dateArray.reverse();



var dateArray1 = [];

$(dateArray).each(function(i){
	var newthisdate = new Date($(this)[0]).toLocaleDateString('en-US', {  month: 'long',day: 'numeric', year: 'numeric' })
console.log(newthisdate);
	dateArray1.push(newthisdate)
})

console.log(dateArray);
function getData() {
	$.ajax({
		type: 'GET',
		url: 'data/item.json',
		dataType: 'json',
		success: function (data) {
			content = data;

			var randomText = content.items; //data
			var newArray = [];
			var arrayOfObj = {};

			var a = Math.random();

			var arrayLength = randomText.length; //array size
			console.log(arrayLength); //comming
			console.log(randomText); //comming// 01

			b = Math.floor(a * arrayLength);


			console.log(typeof b); //random id 1-120


			function randomArray(arr) {
				var currentIndex = arr.length,
					temporaryValue, randomIndex;

				// While there remain elements to shuffle...
				while (0 !== currentIndex) {

					// Pick a remaining element...
					randomIndex = Math.floor(Math.random() * arrayLength);
					currentIndex -= 1;


					// And swap it with the current element.
					temporaryValue = arr[currentIndex];

					arr[currentIndex] = arr[randomIndex];
					arr[randomIndex] = temporaryValue;
				}

				return arr;

			};

			// object
			var newArray = randomArray(Object.values(randomText));
			//console.log(newArray);

			// array of object
			var arrayOfObj = Object.assign({}, newArray);
		//	console.log(typeof arrayOfObj);


			$(newArray).each(function (items) { //replace  randomText[b] with newArray
			//	console.log(items);
				newsItems.push({
					"title": this.title,
					"description": this.description,
					"thumb": this.thumb,
					"date": this.date,
					"updated_at": new Date(this.updated_at),
					"news_type": this.news_type[0][2]
				});
				if (categories.includes(this.news_type[0][2])) {} else {
					categories.push(this.news_type[0][2])
				}
				if (dropyears.includes((newsItems[items].updated_at).getFullYear())) {} else {
					dropyears.push((newsItems[items].updated_at).getFullYear());
				}

				//console.log(items)
			});


			$(categories).each(function () {
				if (this != "") {
					$('#cat').append(`<option>${this}</option`);
				}
			});
			$(dropyears).each(function () {
				$('#year').append(`<option>${this}</option`);
			});
			populateContent();
		},
		error: function (data) {
			alert('json error');
		}
	});
}

function populateContent() {
	if (newsItems.length == 0) {
		$('#more').addClass('disable');
		return
	} else {
		$(newsItems).each(function (i) {
			if (i < itemdisplay) {
				//newsItems.shift();
				//populate(this.thumb, this.date, this.title, this.description);
				populate(this.thumb, dateArray1[i], this.title, this.description);
			}

		});

	}
}

function populate(a, b, c, d) {

	$('#news').append(
		`
								<div class="col-md-12">
									   <hr>
									   <div class="row">
										  <div class="col-md-4">
											 <div class="list_image">
												<img src="${imgprefix+a}">
											 </div>
										  </div>
										  <div class="col-md-8">
										  	<div class="list_text">
											 <div class="list_date">${b}</div>
											 <div class="content_title">${c}</div>
											 <div class="article_teaser_body">${d}</div>
											 </div>
										  </div>
									   </div>
									</div>
						`
	);

}


function randomDate(start, end) {
	var d = new Date(start.getTime() + Math.random() * (end.getTime() - start.getTime())),
		month = '' + (d.getMonth() + 1),
		day = '' + d.getDate(),
		year = d.getFullYear();
	if (month.length < 2) month = '0' + month;
	if (day.length < 2) day = '0' + day;
	return [year, month, day].join('-');
}
