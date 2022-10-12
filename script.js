import http from "k6/http";

export let options = {
    vus: 5,
    stages: [
        // { duration: "3m", target: 5 },
        { duration: "30s", target: 5 },
        // { duration: "10m", target: 35 },
        // { duration: "1m30s", target: 0 },
    ]
};

export default function () {
    var r
    r = http.get("http://192.168.1.46/dummy-16.file");
    // r = http.get("http://192.168.1.46/dummy-32.file");
    // r = http.get("http://192.168.1.46/dummy-128.file");
    r = http.get("http://192.168.1.46/dummy.bin");

};
