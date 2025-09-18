console.log("kurva anyád");

const NEV = "aaaaaa";

console.log("helo " + NEV + " xd");

function hello(nev){
    console.log(nev + " habos");
}

hello("kek");

//2. óra típuskonverzió
{
    let a = 5;
    var b = 6;
    console.log(a);
}
console.log(b);
console.log(parseInt(5/2));// egész szám konverzió xd
console.log(typeof 42.6); // vagy egy típusnevet ad vissza stringként vagy undefined-ot ad vissza
console.log(typeof 42 == "number"); // true mert a typeof 42 egy stringet ad vissza ami típust reprezentál
console.log(42 == "42"); //nem típusellenőrzés - érték true lesz

//ha van string akkor összefűzés valósul meg és ezek stringek lesznek
var tmp = 2 + "5";
var tmp2 = "5" + 2;
console.log(typeof tmp);
console.log(typeof tmp2);
console.log(4 + "5");
console.log("5" + 2);

//ha üres a string vagy csak egy space van akkor 0-át ad vissza (meg a false-ra is)
console.log(Number("42.5"));
var c = Number("42.5 asfsdfg");
console.log(c); // Ha a string végén van extra karakter ami nem lenne konvertálható számba akkor NaN-t ad vissza
console.log(typeof c); // szám típusú

console.log(Boolean("true"));// rendesen konvertálja true-ba
console.log(Boolean("false")); // csak üres string esetében lesz false a boolean konverzió
console.log(Boolean(0)); // ez is false és NaN-ra is false kellene hogy legyen

var d = - "-42"; // number lesz működik a koverzioó stringből számba, ha pedig nem számos szöveget adok hozzá akkor NaN lesz
console.log(typeof d);
console.log(d);

console.log("Ba" + +"asd"+"a"); //az asd a whitespace addition miatt NaN lesz de a stringek hozzá vannak füzve amibol funny text hehe

let alma;
console.log(typeof alma); //Undefined

function calcCircleArea(radius){
    return Math.PI * radius * radius;
}

console.log(calcCircleArea(10));

function kezfogas(emberek){
    let kezfogasCount = 0;
    for(var i = emberek; i > 0; i--){
        for(var y = emberek - 1; y > 0; y--){
            kezfogasCount++;
        }
        emberek--;
    }
    return kezfogasCount;
}

console.log(kezfogas(10));

function egyezes(par1, par2){
    if (typeof par1 == typeof par2 && par1 == par2){
        return true;
    }else{
        return false;
    }
}

console.log(egyezes(true, true));