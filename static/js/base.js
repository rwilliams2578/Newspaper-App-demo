$(document).ready(function () {
    $('.like_button').click(function (event) {
        // The work we want to do on click.

        // Get required data
        let target = $(event.currentTarget);
        let article_id = target.data('id');
        let article_action = target.data('action');
        let article_like_url = target.data('like-url');

        // Get icon and count elements
        let like_icon = target.find('.like_icon');
        let like_count = target.find('.like_count');

        $.ajax({
            url: article_like_url,
            data: {
                article_id: article_id,
                article_action: article_action,
            },
        }).done(function (data) {
            // Do completion work here.
        });
    });
});