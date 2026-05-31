function showPage(page){
    document.querySelectorAll(".page").forEach(p => p.classList.remove("active"));
    document.getElementById(page).classList.add("active");
}

function prediksi(){

    const cuaca = document.getElementById("input_cuaca").value;
    const gelombang = document.getElementById("gelombang").value;
    const hari = document.getElementById("hari").value;
    const penumpang = document.getElementById("penumpang").value;

    // VALIDASI
    if(cuaca === "" || gelombang === "" || hari === "" || penumpang === ""){
        alert("Semua input harus diisi!");
        return;
    }

    fetch("/predict", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({
            cuaca: cuaca,
            gelombang: gelombang,
            hari: hari,
            penumpang: penumpang
        })
    })
    .then(res => res.json())
    .then(data => {
        document.getElementById("hasil").innerHTML = `
        <div class="ticket">
            <h2>Hasil Prediksi</h2>
            <p>Jam Tiba: ${data.jam_tiba}</p>
            <p>Jam Berangkat: ${data.jam_berangkat}</p>
            <p>Jumlah Kapal: ${data.jumlah_kapal}</p>
            <h4>Data diatas merupakan hasil prediksi untuk membantu penumpang estimasikan waktu tiba di pelabuhan , bukan waktu sebenarnya.Tetap berhati-hati di pelabuhan!</h4>
        </div>
        `;
    })
    .catch(err => {
        alert("Terjadi error, pastikan server Flask berjalan!");
        console.log(err);
    });
}