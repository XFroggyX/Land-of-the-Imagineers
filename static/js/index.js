import * as THREE from './three.module.js'
import {THREEx} from './threex.domevents.js'

const canvas = document.querySelector('.canvas');

const renderer = new THREE.WebGLRenderer({antialias: true, canvas});

const scene = new THREE.Scene();
scene.background = new THREE.Color( 0xbfe3dd );

const camera = new THREE.PerspectiveCamera(75, 2, 0.1, 1000);
camera.position.set(0, 10, 0)
camera.lookAt(0, 0,0 )

const light = new THREE.DirectionalLight(0xffffff, 1);
light.position.set(0, 10, 0)

let domEvents = new THREEx.DomEvents(camera, renderer.domElement);

const geometry = new THREE.PlaneGeometry();

const raycaster = new THREE.Raycaster();
const mouse = new THREE.Vector2();


let cubes = [];
const EDGE_LEN = 10;
for(let i = -EDGE_LEN; i < EDGE_LEN; i++)
{
    cubes.push([]);
    for(let j = -EDGE_LEN; j < EDGE_LEN; j++)
    {
        cubes[i + EDGE_LEN].push(makeInstance(geometry, i * 1.01, 0, j * 1.01));
    }

}

function render() {
    raycaster.setFromCamera( mouse, camera );
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
    let material = new THREE.MeshBasicMaterial( { color: 0x45ad4c } );
    const cube = new THREE.Mesh(geometry, material);
    scene.add(cube)

    cube.position.x = x;
    cube.position.y = y;
    cube.position.z = z;

    cube.rotation.x = -1.5708;

    domEvents.addEventListener(cube, 'click', function(event){
    }, false)

    domEvents.addEventListener(cube, 'mouseup', function(event){
        cube.material.color.setHex( 0x19EA29FF );
    }, false)

    domEvents.addEventListener(cube, 'mouseout', function(event){
        cube.material.color.setHex( 0x45ad4c );
    }, false)

    return cube;
}

document.addEventListener('keydown',onDocumentKeyDown,false);
function onDocumentKeyDown(event){
    var delta = 0.1;
    event = event || window.event;
    var keycode = event.keyCode;
    console.log(keycode)
    switch(keycode){
    case 65 :
    camera.position.x = camera.position.x - delta;
    break;
    case 87 :
    camera.position.z = camera.position.z - delta;
    break;
    case 68 :
    camera.position.x = camera.position.x + delta;
    break;
    case 83 :
    camera.position.z = camera.position.z + delta;
    break;
    }
}
function onDocumentKeyUp(event){
    document.removeEventListener('keydown',onDocumentKeyDown,false);
}


requestAnimationFrame(render);