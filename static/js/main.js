window.onload = ()=>{
        window.addEventListener("keydown", (e) => {
            if (e.keyCode == 81){
                radio_tag = document.getElementById(1);
                radio_tag.checked = true;
            } else if ( e.keyCode == 87) {
                radio_tag = document.getElementById(2);
                radio_tag.checked = true;
            } else if (e.keyCode == 69) {
                radio_tag = document.getElementById(3);
                radio_tag.checked = true;
            } else if (e.keyCode == 83) {
                document.submit_name.submit();
            }
            console.log(e.keyCode);
        });
}