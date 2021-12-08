import * as THREE from './three.module.js'
import {THREEx} from './threex.domevents.js'
import {MapControls} from './OrbitControls.js'
import * as jQuery from './jquery-3.6.0.js'

const canvas = document.querySelector('.canvas');
const body = document.querySelector('body');

const renderer = new THREE.WebGLRenderer({antialias: true, canvas});

const scene = new THREE.Scene();
scene.background = new THREE.Color( 0xbfe3dd );

const EDGE_LEN = 20;

const width = canvas.clientWidth;
const height = canvas.clientHeight;

const camera = new THREE.PerspectiveCamera(60, 2, 0.1, 1000);
camera.position.set(EDGE_LEN / 2, 5, EDGE_LEN / 2)


const controls = new MapControls( camera, renderer.domElement );

controls.enableRotate = false
controls.enableZoom = false

controls.mouseButtons = {
	RIGHT: THREE.MOUSE.PAN
}

controls.panSpeed = 2

controls.minDistance = 5;
controls.maxDistance = 5;



const light = new THREE.DirectionalLight(0xffffff, 1);
light.position.set(0, 10, 0)


let domEvents = new THREEx.DomEvents(camera, renderer.domElement);
const geometry = new THREE.PlaneGeometry();

let cubes = [];
for(let i = 0; i < EDGE_LEN; i++)
{
    cubes.push([]);
    for(let j = 0; j < EDGE_LEN; j++)
    {
        cubes[i].push(makeInstance(geometry, i, 0, j));
    }

}

function render() {
    if (resizeRendererToDisplaySize(renderer)) {
        const canvas = renderer.domElement;
        camera.aspect = canvas.clientWidth / canvas.clientHeight;
        camera.updateProjectionMatrix();
    }
    renderer.render(scene, camera);

    requestAnimationFrame(render);
}


function resizeRendererToDisplaySize(renderer) {
    const canvas = renderer.domElement;
    const width = canvas.clientWidth;
    const height = canvas.clientHeight;
    const needResize = canvas.width !== width || canvas.height !== height;
    if (needResize) {
        renderer.setSize(width, height, false);
    }
    return needResize;
}


function makeInstance(geometry, x, y, z) {
    const texture = new THREE.TextureLoader().load('../../static/img/textures/grass(no).png');
    texture.magFilter = THREE.NearestFilter;

    const material = new THREE.MeshBasicMaterial({
        map: texture,
    });



    const cube = new THREE.Mesh(geometry, material);
    console.log(cube)
    scene.add(cube)

    cube.position.x = x;
    cube.position.y = y;
    cube.position.z = z;

    cube.rotation.x = -1.5708;

    domEvents.addEventListener(cube, 'click', function(event){
        console.log(cube.position.x);
        console.log(cube.position.y);
        console.log(cube.position.z);

       var popup = document.createElement("div");
       popup.style.cssText = "position: fixed; top: 40px; left: 40px; height: 200px; width: 400px; background: gray";

       var input = document.createElement("input");
       input.style.cssText = "height: 30%; width: 90%;";
       popup.appendChild(input);

       var button = document.createElement("button");
       button.style.cssText = "height: 30%; width: 90%;";
       popup.appendChild(button);

       button.onclick = function() {
            var val = input.value

            $.ajax({
                url: '/api/',
                method: 'post',
                dataType: 'json',
                data: {name_town: val, point_x: cube.position.x, point_y: cube.position.z},
                success: function(data){
                    cube.material.color.setHex( 0xFF8844 );
                }
            });

            body.removeChild(popup);
        };

       body.appendChild(popup);

    }, false)

    return cube;
}

requestAnimationFrame(render);