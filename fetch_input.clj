#!/usr/bin/env bb

(require '[babashka.curl :as curl]
         '[clojure.java.shell :refer [sh]])

;; set the var(s) from the dotenv
(sh "bash" "-c" "export $(xargs <.env)")

(def current-cookie
  (System/getenv "CURRENT_COOKIE"))

(if (not (nil? current-cookie))
  (println "CURRENT_COOKIE is set!")
  (println "Set your CURRENT_COOKIE first!"))

(def base-url "https://adventofcode.com/")

;; You should pass year and day as command line args
(when (not(nil? current-cookie))
  (let [[year day] *command-line-args*
        ;; TODO?: make this into another function that would print out usage info as well
        complete-url (str base-url year "/day/" day "/input")]
    (println (str "Downloading input for year: " year " day: " day))
    (println (str "fetching input from: " complete-url))
    (spit day (:body (curl/get complete-url {:headers {"cookie" (str "session=" current-cookie)}})))
    ;; move the file to appropriate place
    (sh "mv" (str "./" day) (str "./" year "/" day "/"))))

(println "Done!")

