# Rekognition PPE APIを使ったマスク検知ハンズオン

1. Cloud9を立ち上げる

2. Cloud9のAWS ToolkitからAPI Gateway + Lambdaの構成をデプロイする (`HelloWorldFunction`)

3. ブラウザからGETリクエストを送って`"Hello World!"`というJSONレスポンスが見えるか確認する

4. POSTリクエストを受け取れるように`template.yaml`とLambdaを書き換える

5. HTML/JavaScriptからPOSTリクエストを送って挙動を確認する

6. Rekognition PPE APIをLambdaに組み込んでPOSTリクエストから画像を処理するようLambdaを書き換える

7. Lambdaのエラーを特定し、デバッグする

8. HTML/JavaScriptでレスポンスのJSONを可視化する

