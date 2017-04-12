<!DOCTYPE html>
<html lang="en">
% include('~head.tpl', title='Maria Salem | Resume', description='Event and Venue expert as Customer Experience Manager for a nightlife application with a background in Events and Wedding Coordinating. Hire me!')
  <body class="main">
    % include('~structuredData.tpl')
    <style>
      @media all and (-ms-high-contrast:none) {
        .content.resume > iframe {
          max-width: none;
          height: 100%;
        } /* IE10 */
        *::-ms-backdrop, .content.resume > iframe {
          max-width: none;
          height: 100%;
        } /* IE11 */
      }
    </style>
    <div class="top menu">
      <!--span class="clickable">Home<a href="/"></a></span>
      <span class="divider">|</span-->
      <span class="ion-ios-rose clickable">
        <a href="/"></a>
      </span>
    </div>
    <div class="content resume">
      <!--embed src="resume.pdf" type='application/pdf'-->
      <iframe src="http://docs.google.com/gview?url=http://mariasalem.com/resume.pdf&embedded=true" frameborder="0"></iframe>
    </div>
% include('~footer.tpl')
  </body>
</html>
