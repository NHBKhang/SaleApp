window.onscroll = function () {
    let r = document.getElementById("return")
    if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
        r.style.display = "block";
    } else {
        r.style.display = "none";
    }
}
function scrollToTop()
{
    document.body.scrollTop = 0;
    document.documentElement.scrollTop = 0;
}

function addComment(id) {
    if (confirm("Bạn chắc chắn bình luận?") === true) {
    fetch(`/api/products/${id}/comments`, {
            method: 'post',
            body: JSON.stringify({
                "content": document.getElementById('comment').value
            }),
            headers: {
                'Content-Type': 'application/json'
            }
        }).then(function(res) {
            return res.json();
        }).then(function(data) {
            if (data.status === 200) {
                let c = data.comment;
                let html = document.getElementById("comments");
                html.innerHTML = `
                 <div class="row alert alert-info">
                        <div class="col-md-1 col-xs-4">
                            <img src="${c.user.avatar}" class="img-fluid rounded" />
                        </div>
                        <div class="col-md-11 col-xs-8">
                            <p><strong>${c.user.name}</strong></p>
                            <p>>${c.content}</p>
                            <p>Bình luận lúc: <span class="date">${moment(c.created_date).locale("vi").fromNow()}</span></p>
                        </div>
                    </div>
                ` + html.innerHTML
            } else
                alert(data.err_msg)
        });
    }
}
