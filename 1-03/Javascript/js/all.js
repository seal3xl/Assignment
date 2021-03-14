function getContent(){//建立資料數量的ul>li結構，並將資料逐一放入div中。
//讀取資料。
    var req=new XMLHttpRequest();
    req.open("get","https://padax.github.io/taipei-day-trip-resources/taipei-attractions.json");
    req.onload=function(){
        var data=this.responseText;
        data=JSON.parse(data);
        data=data["result"]["results"];
//建立列表元素。
        for(num=1;num<=data.length;num++){
            var content=document.getElementById("content");
            var li=document.createElement("li");
            var a=document.createElement("a");
            a.setAttribute("href","#");
            var img=document.createElement("img");
            img.setAttribute("src","");
            img.setAttribute("id","img_"+num);
            var div=document.createElement("div");
            div.setAttribute("class","text");
            var h2=document.createElement("h2");
            h2.setAttribute("id","textTitle_"+num)
//建立列表結構。
            div.appendChild(h2);
            a.appendChild(img);
            a.appendChild(div);
            li.appendChild(a);
            content.appendChild(li);
//將讀取的標題逐一放入對應div中。
            var textTitle=document.getElementById("textTitle_"+num);
            textTitle.append(data[num-1]["stitle"]);
//逐一處理圖片連結資料，並放入對應的img標籤中。
            var img_src=data[num-1]["file"];
            img_src=img_src.replace("jpg","jpg,");
            img_src=img_src.replace("JPG","JPG,");
            img_src=img_src.replace("png","png,");
            img_src=String(img_src.split(",",1));
            var imgForm=document.getElementById("img_"+num);
            imgForm.setAttribute("src",img_src);
        }
    };
    req.send();
}


function loadAll(){//點擊後，列出全部的資料。
//讀取資料，計算資料總數。
    var req=new XMLHttpRequest();
    req.open("get","https://padax.github.io/taipei-day-trip-resources/taipei-attractions.json");
    req.onload=function(){
        var data=this.responseText;
        data=JSON.parse(data);
        data=data["result"]["results"];
        var len=data.length;

//判斷目前裝置解析度，展開對應的高度，並將loadmore選單隱藏。
//裝置寬>=1200px
        if(document.body.clientWidth>=1200){
//以4個資料為1個列，判斷總高度(列數)。
            if(len%4==0){
                var contentHeightMax=len/4;
            }
            else{
               var contentHeightMax=len/4;
               contentHeightMax=Math.floor(contentHeightMax);
                contentHeightMax++;
            }
//點擊後至所有資料都列出的對應高度40(contentHeightMax行)*220px=17600px，並將按鈕隱藏。
            var contect=document.getElementById("contentHeight");
            contect.style.height=contentHeightMax*220+"px";//每列220px，共contentHeightMax列。
            var loadmore=document.getElementById("loadmore");
            loadmore.style.display="none";
        }
//600px<=裝置寬<1200px
        else if(document.body.clientWidth>=600){
//以2個資料為1個列，判斷總高度(列數)。
            if(len%2==0){
                var contentHeightMax=len/2;
            }
            else{
            var contentHeightMax=len/2;
            contentHeightMax=Math.floor(contentHeightMax);
                contentHeightMax++;
            }
//點擊後至所有資料都列出的對應高度160(contentHeightMax行)*220px=35200px，並將按鈕隱藏。
            var contect=document.getElementById("contentHeight");
            contect.style.height=contentHeightMax*220+"px";
            var loadmore=document.getElementById("loadmore");
            loadmore.style.display="none";
        }
//裝置寬<600px
        else{
//總列數為資料數(1列1個資料)，故以len代表總列數。
//點擊後至所有資料都列出的對應高度319(contentHeightMax行)*220px=70180px，並將按鈕隱藏。
            var contect=document.getElementById("contentHeight");
            contect.style.height=len*220+"px";
            var loadmore=document.getElementById("loadmore");
            loadmore.style.display="none";
        }
    }
    req.send();
}

function loadMore(){//點擊後，列出更多的資料。
//讀取資料，計算資料數。
        var req=new XMLHttpRequest();
        req.open("get","https://padax.github.io/taipei-day-trip-resources/taipei-attractions.json");
        req.onload=function(){
            var data=this.responseText;
            data=JSON.parse(data);
            data=data["result"]["results"];
            var len=data.length;

//判斷目前裝置解析度，展開對應的高度，並將loadmore選單隱藏。
//裝置寬>=1200px
        if(document.body.clientWidth>=1200){
//以4個資料為1個單位，判斷總列數。
            if(len%4==0){
                var contentHeightMax=len/4;
            }
            else{
                var contentHeightMax=len/4;
                contentHeightMax=Math.floor(contentHeightMax);
                contentHeightMax++;
            }
//點擊後1次增加2列(8個資料)的高度。
            var contentHeight=document.getElementById("contentHeight").offsetHeight;
            var contect=document.getElementById("contentHeight");
            contect.style.height=contentHeight+440+"px";
            contentHeight+=440;
//若增加的高度高過總列數，將按鈕隱藏，並將高度設為總列數相應的高度。
            if(contentHeight>=contentHeightMax*220){
                var loadmore=document.getElementById("loadmore");
                loadmore.style.display="none";
                contect.style.height=contentHeightMax*220+"px";
                }
            }
//600px<=裝置寬<1200px
        else if(document.body.clientWidth>=600){
//以2個資料為1個單位，判斷總列數。
            if(len%2==0){
                var contentHeightMax=len/2;
            }
            else{
                var contentHeightMax=len/2;
                contentHeightMax=Math.floor(contentHeightMax);
                contentHeightMax++;
            }
//點擊後1次增加4列(8個資料)的高度。
            var contentHeight=document.getElementById("contentHeight").offsetHeight;
            var contect=document.getElementById("contentHeight");
            contect.style.height=contentHeight+880+"px";
            contentHeight+=880;
//若增加的高度高過總列數，將按鈕隱藏，並將高度設為總列數相應的高度。
            if(contentHeight>=contentHeightMax*220){
                var loadmore=document.getElementById("loadmore");
                loadmore.style.display="none";
                contect.style.height=contentHeightMax*220+"px";
            }
        }
//裝置寬<600px
        else{
//總列數為資料數(1列1個資料)，故以len代表總列數。
//點擊後1次增加8列(8個資料)的高度。
            var contentHeight=document.getElementById("contentHeight").offsetHeight;
            var contect=document.getElementById("contentHeight");
            contect.style.height=contentHeight+1760+"px";
            contentHeight+=1760;
//若增加的高度高過總列數，將按鈕隱藏，並將高度設為總列數相應的高度。
            if(contentHeight>=len*220){
                var loadmore=document.getElementById("loadmore");
                loadmore.style.display="none";
                contect.style.height=len*220+"px";
            }
        }
    }
    req.send();
}