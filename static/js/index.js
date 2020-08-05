$(document).ready(function() {
  $('#document').on("mouseover", '.wiki', wikiHovered);
});

function gen_entity_linking(){
  let readerBox = document.getElementById("document");
  let paragraphs = readerBox.getElementsByTagName("p");

  for (let paragraph of paragraphs){
    ner(paragraph, replace_text);
  }
}

function ner(paragraph, success_function){
    $.ajax({
        type: "POST",
        url: "/gen_el/",
        dataType: 'json',
        data: JSON.stringify({'paragraph': paragraph.innerText}),
        success: (function(paragraph) {
            return (data) => success_function(data, paragraph);
        })(paragraph),
    });
}

function replace_text(data, paragraph){
  paragraph.innerHTML = data.paragraph;
  let entitySpan = paragraph.getElementsByClassName('entity');
  let detectEntity = data.entity;

  let count = 0;

  for (let entityIdx of detectEntity){
    let index = entityIdx[0];
    let entityTitle = entityIdx[1];

    while ( count != index ){
      count++;
    }
    let entity = entitySpan.item(count);
    let wikiURL = `https://zh.wikipedia.org/wiki/${entityTitle}`
    entity.innerHTML = `<a class="wiki" target="_blank" href="${wikiURL}" title="${entityTitle}"
      data-title="${entityTitle}"
      data-toggle="popover" data-trigger="hover" data-placement="bottom">${entity.innerHTML}</a>`
  }
}