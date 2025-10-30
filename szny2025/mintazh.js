// Nev: Kis Bence RĂłbert
// Neptun: IFQA67
// h: h264560

class Fuzet {
    constructor(tipus, oldalak_szama = 8) {
        this._tipus = tipus;
        this._oldalak_szama = oldalak_szama;
        this._rajzok = [];
    }

    get oldalak_szama(){
        return this._oldalak_szama;
    }

    set oldalak_szama(newParam){
        if(this._oldalak_szama <= newParam){
            this._oldalak_szama = newParam;
        }
    }

    tipus_valtas(type){
        if(this._tipus !== type){
            this._tipus = type;
            this._rajzok = [];
        }
    }

    rajzok_listaja(){
        let tmp = this._rajzok.sort();
        var stringOut = "";
        for(let i = 0; i < tmp.length; i++){
            if(i === tmp.length - 1){
                stringOut += tmp[i];
            }else{
                stringOut += (tmp[i] + ", ");
            }
        }
        return stringOut;
    }

    uj_rajz(rajzok){
        if(typeof rajzok === "string"){
            this._rajzok.push(rajzok);
        }else if(Array.isArray(rajzok)){
            this._rajzok.push(...rajzok);
        }
        return this._rajzok.length;
    }

    varazslat(rajzok, callback){
        if(!Array.isArray(rajzok) || typeof callback !== "function"){
            return false;
        }

        const findAllRajz = rajzok.every(r => this._rajzok.includes(r));

        if(findAllRajz){
            callback(this);
            return true;
        }
        return false;
    }
}

function varazslatok(objects){
    if(!Array.isArray(objects)){
        return undefined;
    }

    return objects
        .filter(e => e.tipus === "tuz" && e.erosseg >= 5)
        .map(e => e.nev);
}