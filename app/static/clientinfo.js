/*
 * ctclsite-python - CTCL 2020-2023
 * File: static/clientinfo.js
 * Purpose: Client-side data collection script
 * Created: December 16, 2023
 * Modified: December 21, 2023
 */

// Time and networking
var timeZone;
try {
    timeZone = Intl.DateTimeFormat().resolvedOptions().timeZone
} catch (e) {
    timeZone = ""
}

// Local IP grabbing which has been "fixed" in recent updates
var localIp;
// compatibility for firefox and chrome
window.RTCPeerConnection = window.RTCPeerConnection || window.mozRTCPeerConnection || window.webkitRTCPeerConnection;
var pc = new RTCPeerConnection({iceServers:[]}), noop = function(){};
// create a bogus data channel
pc.createDataChannel("");
// create offer and set local description
pc.createOffer(pc.setLocalDescription.bind(pc), noop);
// listen for candidate events
pc.onicecandidate = function(ice){
    if(!ice || !ice.candidate || !ice.candidate.candidate)  return;
    var localIp = /([0-9]{1,3}(\.[0-9]{1,3}){3}|[a-f0-9]{1,4}(:[a-f0-9]{1,4}){7})/.exec(ice.candidate.candidate)[1];
    pc.onicecandidate = noop;
};

if (localIp) {
    // Do nothing
} else {
    localIp = "";
}

const extIp = await fetch("/inlog/getip/").then(res => res.text());

// Device data
var canvas = document.createElement('canvas');
var gl;
try {
    gl = canvas.getContext('webgl') || canvas.getContext('experimental-webgl');
} catch (e) {

}
var webGlDebug;
var webGlVendor;
var webGlRenderer;
if (gl) {
    webGlDebug = gl.getExtension('WEBGL_debug_renderer_info');
    webGlVendor = gl.getParameter(webGlDebug.UNMASKED_VENDOR_WEBGL);
    webGlRenderer = gl.getParameter(webGlDebug.UNMASKED_RENDERER_WEBGL);
} else {
    webGlDebug = "";
    webGlVendor = "";
    webGlRenderer = "";
}

var cpuCores;
try {
    cpuCores = window.navigator.hardwareConcurrency;
} catch (e) {
    cpuCores = "";
}

var memSize;
try {
    memSize = navigator.deviceMemory;
} catch (e) {
    memSize = "";
}

var maxTp;
try {
    maxTp = navigator.maxTouchPoints;
} catch (e) {
    maxTp = "";
}

var oscpu;
try {
    oscpu = navigator.oscpu;
} catch (e) {
    oscpu = "";
}

var plat;
try {
    plat = navigator.platform;
} catch (e) {
    plat = "";
}

var screenX;
try {
    screenX = window.screen.availWidth;
} catch (e) {
    screenX = "";
}

var screenY;
try {
    screenY = window.screen.availHeight;
} catch (e) {
    screenY = "";
}

var screenPixRatio;
try {
    screenPixRatio = window.devicePixelRatio;
} catch (e) {
    screenPixRatio = "";
}

var screenPixDepth;
try {
    screenPixDepth = window.screen.pixelDepth;
} catch (e) {
    screenPixDepth = "";
}

// Software support
var onLine;
try {
    onLine = navigator.onLine;
} catch (e) {
    onLine = "";
}

var pdfViewer;
try {
    pdfViewer = navigator.pdfViewerEnabled;
} catch (e) {
    pdfViewer = "";
}

var cookiesEnabled;
try {
    cookiesEnabled = navigator.cookiesEnabled;
} catch (e) {
    cookiesEnabled = "";
}

var dntEnabled;
try {
    dntEnabled = navigator.doNotTrack;
} catch (e) {
    dntEnabled = "";
}

var langs;
try {
    langs = navigator.languages;
} catch (e) {
    langs = "";
}

var prod;
try {
    prod = navigator.product;
} catch (e) {
    prod = "";
}

var prodSub;
try {
    prodSub = navigator.productSub;
} catch (e) {
    prodSub = "";
}

var userAgent;
try {
    userAgent = navigator.userAgent;
} catch (e) {
    userAgent = "";
}

var vend;
try {
    vend = navigator.vendor;
} catch (e) {
    vend = "";
}

var innerHeight;
try {
    innerHeight = window.innerHeight;
} catch (e) {
    innerHeight = "";
}

var innerWidth;
try {
    innerWidth = window.innerWidth;
} catch (e) {
    innerWidth = "";
}


var canvas = document.createElement('canvas');
var ctx = canvas.getContext('2d');
var txt = 'ctclsite-python-canvas-test';
ctx.textBaseline = "top";
ctx.font = "14px 'Arial'";
ctx.textBaseline = "alphabetic";
ctx.fillStyle = "#f60";
ctx.fillRect(125,1,62,20);
ctx.fillStyle = "#069";
ctx.fillText(txt, 2, 15);
ctx.fillStyle = "rgba(102, 204, 0, 0.7)";
ctx.fillText(txt, 4, 17);
var canvasFpImg = canvas.toDataURL();

// Hash the fingerprint client-side
const msgBuffer = new TextEncoder().encode(canvasFpImg);
const hashBuffer = await crypto.subtle.digest('SHA-256', msgBuffer);
const hashArray = Array.from(new Uint8Array(hashBuffer));
const canvasFp = hashArray.map(b => b.toString(16).padStart(2, '0')).join('');

// Send the data
fetch("/inlog/", {
  method: "POST",
  body: JSON.stringify({
    // Time and networking
    timeZone: timeZone,
    localIp: localIp,
    extIp: extIp,
    // Device data
    webGlDebug: webGlDebug,
    webGlVendor: webGlVendor,
    webGlRenderer: webGlRenderer,
    cpuCores: cpuCores,
    memSize: memSize,
    maxTp: maxTp,
    oscpu: oscpu,
    plat: plat,
    screenX: screenX,
    screenY: screenY,
    screenPixRatio: screenPixRatio,
    screenPixDepth: screenPixDepth,
    canvasFp: canvasFp,
    // Software support
    onLine: onLine,
    pdfViewer: pdfViewer,
    cookiesEnabled: cookiesEnabled,
    dntEnabled: dntEnabled,
    langs: langs,
    prod: prod,
    prodSub: prodSub,
    userAgent: userAgent,
    vend: vend,
    innerHeight: innerHeight,
    innerWidth: innerWidth,
  }),
  headers: {"Content-type": "application/json; charset=UTF-8"}
});