import * as jQuery from './jquery-3.6.0.js'

const main = document.querySelector('main');

$.ajax({
	url: '/api/current_user/',
	method: 'get',
	dataType: 'json',
	success: function(data){
        console.log(data.username);
    }
  });


let mass = {
    1: {
        "nameBuild": "Замок",
        "lvl": 2
    },
    2: {
        "nameBuild": "Казарма",
        "lvl": 2
    },
    3: {
        "nameBuild": "Склад",
        "lvl": 2
    }
}


let len = Object.keys(mass).length;

for (let i = 1; i < len + 1; i++) {
    console.log(mass[i].nameBuild);
    console.log(mass[i].lvl);
    add_buildings(mass[i].nameBuild);
}

function add_buildings(build) {

    let name_build = build;
    let img_src;

    if (build == "Замок") {
        img_src = "/static/img/castle.png";
    } else if (build == "Казарма") {
        img_src = "/static/img/barracks.png";
    } else if (build == "Склад") {
        img_src = "/static/img/storage.png";
    }

    var build = document.createElement("section");
    build.innerHTML = '' +
                '<div>' +
    		    '<h3>' + name_build + '</h3>' +
				'<img src="'+ img_src + '">'+
				'</div>';

    main.appendChild(build);
}