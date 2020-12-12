#!/usr/bin/env bb

(require '[babashka.curl :as curl]
         '[clojure.java.shell :refer [sh]]
         '[clojure.string :as str])
(import java.util.Date)

(def current-cookie
  (System/getenv "AOC_COOKIE"))

(if current-cookie
  (println "COOKIE is set!")
  (do
    (println "Set your AOC_COOKIE first!")
    (System/exit 1)))

(def date-split 
  (str/split (.toString (java.util.Date.)) #" "))

;; maybe not the best idea to get the current year and date
(def day
  (get date-split 2))

(def year
  (get date-split 5))

(def base-url "https://adventofcode.com/")

(defn make-api-call [y d]
  (let [complete-url (str base-url y "/day/" d "/input")]
    (println (str "Downloading input for year: " y " day: " d))
    (spit (str d ".in") (:body (curl/get complete-url {:headers {"cookie" (str "session=" current-cookie)}})))
    (sh "mv" (str "./" (str d ".in")) (str "./" y "/" d "/"))))

(defn print-usage []
  (println "Usage: ")
  (println "\t COMMAND `year` `day` ")
  (println "NOTE: If you don't provide the year or the day, the current year or the current date will be considered")
  (println "")
  (println ""))

(if-let [[y_flag d_flag] *command-line-args*]
  (do
    (when (nil? y_flag)
      (make-api-call year d_flag))
    (when (nil? d_flag)
      (make-api-call y_flag day))
    (make-api-call y_flag d_flag))
  ;; otherwise just make a call for today
  (do
    (print-usage)
    (make-api-call year day)))

(println "Done!")
