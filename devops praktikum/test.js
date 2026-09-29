const tambah = require('./app');

const hasil = tambah(2, 3);

if (hasil !== 5) {
    throw new Error('Test gagal');
}

console.log('Test berhasil');