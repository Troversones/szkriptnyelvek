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