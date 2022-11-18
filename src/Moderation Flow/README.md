#  Moderation Flow

The below diagram shows the flow of the moderation system we propose. There are four stages included, which are license check, version check, Quality check, and similarity check.

* License check:
Moderators check the license based on the information provided by uploaders. If moderators have doubts, they can contact the uploader for more information.

* Version check:
Moderators check the version from three aspects, "uploaders", "title" and "content". When the uploader, title, and content are exactly. This uploaded content would be judged as duplicated. If the uploader and title are the same, but only most content is the same. Moderators could archive the older version and continue reviewing the newer version.

* Quality check:
The judgment criteria of the quality check mainly focus on topic fitness and confirm whether all selected attributes are suitable. At this stage, moderators check the tags defined by uploaders as well. They are welcome to add more tags as long as the number of tags is less than five.

* Quality check:
Moderators check the similarity according to the result from AI-check. Moderators could define a specific score/percentage. Once the score/percentage of similarity exceeds the defined score/percentage. Moderators could contact uploaders for further discussion and merge it with other suggested similar content.


![Moderation System](https://user-images.githubusercontent.com/80690817/202767447-97893836-afe3-49ae-b726-f73f549e8816.png)
