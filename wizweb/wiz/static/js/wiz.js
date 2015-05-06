var WIZ = WIZ || {};

(function(wiz,$){
    function EventGallery(parent,galleryData){
        if(parent && galleryData){
            var ulStr = '<ul class="gallery">';
            var liStr = "";
            for(var i=0,len=galleryData.length;i<len;i++){
                var item = galleryData[i];
                liStr += '<li><img style="border:1px solid black;" src="/static/images/event/' + item.year +  '/' + item.image + '"/></li>';
            }

            ulStr += liStr;
            ulStr += "</ul>";
            parent.empty();
            parent.append(ulStr);
        }
    }

    EventGallery.prototype = {
        "constructor":EventGallery
    };

    wiz.EventGallery = EventGallery;
})(WIZ,jQuery);