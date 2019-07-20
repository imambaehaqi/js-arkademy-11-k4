let bio = {
    name: "Imam Baehaqi",
    age: 21,
    address: "Dusun Pandean RT 12 RW 04 Gang III No. 47 Desa Ngingas Kecamatan Waru Kabupaten Sidoarjo",
    hobbies: ["Reading", "Football", "Organization"],
    is_married: false,
    list_school: [
    {name: "MINU Ngingas", major: "Madrasah Ibtida'iyah", year_in: 2003, year_out: 2009},
    {name: "MTs Darul Ulum Kureksari", major: "Madrasah Tsanawiyah", year_in: 2009, year_out: 2012},
    {name: "SMKN 2 Buduran", major: "Multimedia", year_in: 2012, year_out: 2015},
    {name: "Universitas 17 Agustus 1945 Surabaya", major:"Teknik Informatika", year_in: 2016, year_out: null}
    ],
    skills: [
    {skill_name: "writing", level: "advance"},
    {skill_name: "programming", level: "beginner"}
    ],
    interest_in_coding:  true
}

let biodata = JSON.stringify(bio);
console.log(biodata);