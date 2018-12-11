git apply <<EOF
diff --git a/guis/browser/client/src/config.js b/guis/browser/client/src/config.js
index 67360e6..27d7bd4 100644
--- a/guis/browser/client/src/config.js
+++ b/guis/browser/client/src/config.js
@@ -1,6 +1,6 @@
 
 class Config{
-  static host = "";
+  static host = "http://127.0.0.1:8000";
 }
 
 export default Config
EOF