function appendHistory(type, query, uuid) {
    if (query == '' || !uuid) return;
    if (type == 0) {
        //用户
        $('.history').append(`
        <div class="right"><div class="bubble bubble-green"><div class="bubble-avatar"><i class="fas fa-user"></i></div><p style="text-align: left" id="${uuid}">${query}</p></div></div>
        `);
    } else {
        //机器人
        $('.history').append(`
        <div class="left"><div class="bubble bubble-white"><div class="bubble-avatar"><image src="./static/lingkong.png" width="80px"></image></div><p style="text-align: left" id="${uuid}">${query}</p></div></div>
        `);
    }
    var scrollHeight = $('.history').prop('scrollHeight');
    $('.history').scrollTop(scrollHeight, 500);
}

function getHistory() {
    $.ajax({
        url: '/history',
        type: 'GET',
        success: function(res) {
            res = JSON.parse(res);
            if (res.code == 0){
                historyList = JSON.parse(res.history);
                for (let i=0; i<historyList.length; ++i) {
                    h = historyList[i];
                    // 是否已创建
                    if (!$('.history').find('#'+h['uuid']).length>0)  {
                        //判断后进行添加
                        appendHistory(h['type'], h['text'], h['uuid']);
                    }
                }
            } else{
                console.error('get history error!')
            }
        },
        error: function() {
            console.error('get history error!')
        }
    })
}

$(function() {
    setInterval('getHistory();', 500)
    $('.CHAT').on('click', function(e) {
        e.preventDefault();
        var query = $('input#query')[0].value;
        $('input#query').val('');
        args = {'query': query}
        $.ajax({
            url: '/chat',
            type: 'POST',
            data: $.param(args),
            success: function(res) {
                var data = JSON.parse(res);
                if (data.code == 0) {
                    console.log('指令发出去啦！');
                } else {
                    console.error('骚凹瑞，指令发不出去诶。。。');
                }
            },
            error: function() {
                console.error('骚凹瑞，指令发不出去诶。。。');
            }
        })
    });
});