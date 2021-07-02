// tiny editior Plugin and js code 

document.addEventListener("DOMContentLoaded",function(event){
    console.log("hlelo form admin");
    let sc = document.createElement('script')
    sc.setAttribute('src','https://cdn.tiny.cloud/1/no-api-key/tinymce/5/tinymce.min.js');

    document.head.appendChild(sc);
    sc.onload = ()=>{
    //     tinymce.init({
    //         selector: '#id_content'
    //       });
          

    tinymce.init({
    selector: '#id_content',
    mobile: {
    }, 
    toolbar: 'undo redo | bold italic underline strikethrough | fontselect fontsizeselect formatselect | alignleft aligncenter alignright alignjustify | outdent indent |  numlist bullist checklist | forecolor backcolor casechange permanentpen formatpainter removeformat | pagebreak | charmap emoticons | fullscreen  preview save print | insertfile image media pageembed template link anchor codesample | a11ycheck ltr rtl | showcomments addcomment',
    autosave_ask_before_unload: true,
    autosave_interval: '30s',
    autosave_prefix: '{path}{query}-{id}-',
    autosave_restore_when_empty: false,
    autosave_retention: '2m',
    image_advtab: true,
    });
    }
    
});
