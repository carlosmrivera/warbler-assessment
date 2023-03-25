$(document).ready(function() {
    $body = $("body");

    // like url
    const add_like_url = '/users/add_like/' // append post id
    const remove_like_url = '/users/remove_like/' //append post id

    $body.on("click", "button.like-btn", function(e) {
        const $el = $(this)
        const isLiked = $el.data('is-liked')
        const message_id = $el.data('message-id')

        $el.hasClass('btn-own-message') && alert('This was intentionally shown to you to test server validation. You cannot like your own message. :)')

        if (isLiked === 'True') {
            // remove like
            $.ajax({
                url: `${remove_like_url}${message_id}`,
                type: 'POST',
                success: function({ success }) {
                    if(success) {
                        $el.data('is-liked', 'False')
                        //toggle liked class
                        $el.toggleClass('liked')
                    }
                },
                error: function({ responseJSON: { error } }) {
                    alert(error ?? 'Something went wrong. Please try again later.')
                }
            })
        } else {
            // add like
            $.ajax({
                url: `${add_like_url}${message_id}`,
                type: 'POST',
                success: function({ success }) {
                    if(success) {
                        $el.data('is-liked', 'True')
                        //toggle liked class
                        $el.toggleClass('liked')
                    }
                },
                error: function({ responseJSON: { error } }) {
                    alert(error ?? 'Something went wrong. Please try again later.')
                }
            })
        }
        
    })
});