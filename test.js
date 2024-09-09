//first example
let szam = 10;

function kezfogas(szam){
    let kezfogasok = 0;
    szam -= 1;
    for (let index = szam; index > 0; index--) {
        kezfogasok += szam;
        szam -= 1;
    }
    return kezfogasok;
}

let i = kezfogas(10);

console.log(i);
//second
let v1 = false;
let v2 = false;

function egykezes(v1,v2){
    return v1 === v2 ? true : false;
}

let i2 = egykezes(v1,v2);

console.log(i2);
//third
let nev = "va";

function udvozol(nev){
    console.log("udvozoljuk " + nev + " varosaban!");
}

udvozol(nev);
//fourth
let xd = "Ferenc";
let xd2 = "NemFerenc";

function kedves(xd){
    if(xd == "" && xd == null){
        return null;
    }else if(xd != "Ferenc"){
        return false;
    }else{
        return true;
    }
}

console.log(kedves(xd));
console.log(kedves(xd2));
//fifth
let also = 10;
let felso = 100;

let osszeg = 0;

function kobosszeg(also, felso){
    for (let index = also - 1; index < felso + 1; index++) {
        osszeg += Math.pow(index,3);
    }
    console.log(osszeg);
}

kobosszeg(also,felso);
//sixth

let x1 = 100;
let x2 = 10;


function kobosszegCall(x1,x2,callback){
    callback(x2,x1);
}
//seventh
