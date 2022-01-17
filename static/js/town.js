import * as jQuery from './jquery-3.6.0.js'

const main = document.querySelector('main');

console.log(123);

let id = 0;
let username = "";
$.ajax({
	url: '/api/current_user/',
	method: 'get',
	dataType: 'json',
	success: function(data){
        id = data.id;
        username = data.username;

        $.ajax({
            url: '/api/struct/'+ id +'/create_unit/',
            method: 'post',
            dataType: 'json',
            data: {
                csrfmiddlewaretoken: document.querySelector('[name=csrfmiddlewaretoken]').value,
                unit_id: 1
            },
            success: function(data){
            }
        });

    }
});





let townsID = 0;
let countBuild = 0;

let obj;


$.ajax({
	url: '/api/user_list/',
	method: 'get',
	dataType: 'json',
	success: function(data){
        for(let i = 0; i < data.length; ++i) {
            if(data[i].UsersID == id)
            {
               townsID = data[0].TownsID;

               $.ajax({
                    url: '/api/struct/' + townsID +'/',
                    method: 'get',
                    dataType: 'json',
                    success: function(data){
                        let len = 1;
                        for(; len < Object.keys(data.points).length; ++len) {
                            if($.isEmptyObject(data.points[len]))
                                break;
                        }

                        countBuild = len - 1;

                        console.log(countBuild);
                        obj = data;

                        iron.textContent = obj.iron;
                        wood.textContent = obj.wood;
                        stone.textContent = obj.stone;

                        for (let i = 1; i < len; i++) {
                            view_buildings(data.points[i].nameBuild);
                        }
                    }
                });

            }
        }
    }
});


const castle = document.querySelector('#castle');
const barracks = document.querySelector('#barracks');
const storage = document.querySelector('#storage');

var unit = document.querySelector('#unit');
var iron = document.querySelector('#iron');
var wood = document.querySelector('#wood');
var stone = document.querySelector('#stone');






castle.onclick = function() {
    add_buildings("Замок");
};

barracks.onclick = function() {
    add_buildings("Казарма");
};

storage.onclick = function() {
    add_buildings("Склад");
};





function view_buildings(build) {

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
};

console.log({});
function add_buildings(build) {
    obj.points[countBuild + 1].nameBuild = "Замок";
    obj.points[countBuild + 1].lvl = 1;

    var points_ = {
        1: {
        },
        2: {
        },
        3: {
        },
        4: {
        },
        5: {
        },
        6: {
        }
    };

    alert(countBuild);
    for(let i = 1; i <= countBuild + 1; ++i)
    {
        points_[i].nameBuild = obj.points[i].nameBuild;
        points_[i].lvl = obj.points[i].lvl;
    }

    console.log(points_);

    if(countBuild < 6) {
        $.ajax({
            url: '/api/struct/' + townsID +  '/edit_town/',
            method: 'post',
            dataType: 'json',
            data:{
                csrfmiddlewaretoken: document.querySelector('[name=csrfmiddlewaretoken]').value,
                townName: obj.townName,
                wood: obj.wood,
                iron: obj.iron,
                stone: obj.stone,
                points: points_
            },
            success: function(data){
                alert("YES");
            },
            error: function(data){
                console.log(data);
                console.log(obj.points);
            }
            });
    }
}