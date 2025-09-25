//vezérlési szerkezetek 3. óra
let szam = 5;

if(szam < 5){
    console.log("kisebb mint 5");
}else if(szam > 5){
    console.log("nagyobb mint 5");
}else{
    console.log("a szám: 5");
}

switch (szam){
    case 1:
        console.log("1");
        break;
    case 2:
        console.log("2");
        break;
    case 3:
        console.log("3");
        break;
    case 4:
        console.log("4");
        break;
    default:
        console.log("asd");
        break;
}

for(let i = 0; i < szam;i++){
    console.log(i);
}

while(szam < 10){
    szam++;
    if(szam % 3 === 0){
        continue;
    }
    console.log(szam * 2);
}
console.log("--------------")
do{
    console.log(szam);
}while(szam < 5)

function f(nev = "Gabor"){
    if(typeof nev == "undefined"){
        console.log("Nem adtal meg nevet");
        return;
    }else if(typeof nev !== "string"){
        console.log("Nem szoveget adtal meg");
        return;
    }
    console.log(nev);
}

f("Pityesz");
f();
f(5);

function f2(nev, kor){
    if(arguments.length != 2){
        console.log("Hianyzo adatok");
        return;
    }
    console.log(`A nevem ${nev} es a korom: ${kor}`);
}

f2("Pityesz", 30);
f2("a");

let osszeg = function (a, b) { return a + b;};
let osszeg2 = (a, b) => {return a + b;};
let osszeg3 = (a, b) => a + b;

console.log(osszeg(6,7));
console.log(((a,b) => {return a + b;})(6, 9));

