
var WikiSummaryTable = {}

function wikiHovered() {
    if (this.title && !$(this).data('content')) {
        $.ajax({
            type: "GET",
            url: "https://zh.wikipedia.org/w/api.php",
            data: {
                format: "json",
                action: "query",
                prop: "extracts",
                titles: this.title,
                origin: "*",
                exintro: "",
                explaintext: "",
                redirects: 1
            },
            dataType: 'jsonp',
            success: (function(ele) {
                return (data) => onWikiAbsSuccess(data, ele);
            })(this),
        });
    }
}

function onWikiAbsSuccess(data, ele) {
    for (let pageid in data.query.pages) {
        let page = data.query.pages[pageid];
        // TODO : Sentence tokenizer needs improvement.
        let sentence =  page.extract.match( /[^。]+[。]+/g )[0];
        WikiSummaryTable[page.title] = sentence;
        // set content of all .wiki with the same title
        // TODO: handle elements title with underlines
        $(`a.wiki[title="${page.title}"]`).data('content', sentence).popover();
        $(ele).filter(":hover").popover('show');
        break;
    }
}