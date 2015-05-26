% include('_header.tpl')

    <div class="row">
        <div class="col-md-12">
            <div class="error-template">
                <h1>Oops!</h1>
                <h2>{{error.status}}</h2>
                <div class="error-details">
                    Sorry, an error has occured,
                    % if error.status == '404 Not Found':
                         Requested page not found!
                    %else:
                         Retry!
                    %end
                </div>
                <div class="error-actions">
                    <a href="/" class="btn btn-primary btn-lg"><span class="glyphicon glyphicon-home"></span>
                        Take Me Home </a><a href="mailto:support@example.com" class="btn btn-default btn-lg"><span class="glyphicon glyphicon-envelope"></span> Contact Support </a>
                </div>
            </div>
        </div>
    </div>

% include('_footer.tpl')
