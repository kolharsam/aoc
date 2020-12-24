package main

import (
	"fmt"
	"io/ioutil"
	"strconv"
	"strings"
)

type action string

const (
	begins action = "begins"
	wakes  action = "wakes"
	asleep action = "asleep"
)

type date struct {
	year  int
	day   int
	month int
}

type guard struct {
	id     int
	events []event
}

type time struct {
	hour   int
	minute int
}

type event struct {
	time   time
	action action
}

func parseDate(dateStr string) date {
	dt := date{}
	strList := strings.Split(dateStr, "-")

	year, err := strconv.Atoi(strings.Split(strList[0], "[")[1])
	if err != nil {
		fmt.Println("failed to convert the year")
	}
	dt.year = year
	month, err := strconv.Atoi(strList[1])
	if err != nil {
		fmt.Println("failed to convert the month")
	}
	dt.month = month
	day, err := strconv.Atoi(strList[2])
	if err != nil {
		fmt.Println("failed to convert the day")
	}
	dt.day = day

	return dt
}

func parseTime(timeStr string) time {
	ti := time{}

	timSpl := strings.Split(timeStr, ":")
	hr, err := strconv.Atoi(timSpl[0])
	if err != nil {
		fmt.Println("failed to convert the hour")
	}
	ti.hour = hr
	min, err := strconv.Atoi(timSpl[1])
	if err != nil {
		fmt.Println("failed to convert the minute")
	}
	ti.minute = min

	return ti
}

func parseInput(filename string) (map[date]guard, map[int]int) {
	buf, err := ioutil.ReadFile(filename)
	if err != nil {
		fmt.Println("Failed to read file")
	}
	lines := strings.Split(string(buf), "\n")
	eventMap := make(map[date]guard)
	guardSleepMap := make(map[int]int)
	for _, v := range lines {
		spl := strings.Split(v, "] ")
		eventStr := spl[1]
		dateAndTime := strings.Split(spl[0], " ")
		dt := parseDate(dateAndTime[0])
		ti := parseTime(dateAndTime[1])
		gNum := -1
		act := begins

		eventStr = strings.Trim(eventStr, " ")

		if strings.Contains(eventStr, string(wakes)) {
			act = wakes
		} else if strings.Contains(eventStr, string(asleep)) {
			act = asleep
		}

		if act == begins {
			sp := strings.Split(eventStr, " ")
			n, err := strconv.Atoi(strings.Split(sp[1], "#")[1])
			if err != nil {
				fmt.Println("failed to convert guard number")
			}
			gNum = n

			if ti.hour == 23 {
				ti.hour = 0
				ti.minute = 0
				dt.day++
			}

			even := event{
				time:   ti,
				action: begins,
			}

			if _, ok := eventMap[dt]; !ok {
				eventMap[dt] = guard{
					id:     gNum,
					events: []event{even},
				}
			} else {
				currentEvents := eventMap[dt].events
				currentEvents = append(currentEvents, even)
				currentEvents = sortEventsByTime(currentEvents)

				eventMap[dt] = guard{
					id:     gNum,
					events: currentEvents,
				}
			}

			if _, ok := guardSleepMap[gNum]; !ok {
				guardSleepMap[gNum] = 0
			}
		} else {
			ev := wakes
			if act == asleep {
				ev = asleep
			}
			current := eventMap[dt].events
			current = append(current, event{
				time:   ti,
				action: ev,
			})
			current = sortEventsByTime(current)
			if _, ok := eventMap[dt]; !ok {
				eventMap[dt] = guard{
					id:     -1,
					events: current,
				}
			} else {
				eventMap[dt] = guard{
					id:     eventMap[dt].id,
					events: current,
				}
			}
		}
	}

	return eventMap, guardSleepMap
}

func sortEventsByTime(events []event) []event {
	sortedEvents := make([]event, len(events))
	copy(sortedEvents, events)

	for i := 0; i < len(sortedEvents); i++ {
		for j := 0; j < len(sortedEvents); j++ {
			if i == j {
				continue
			}
			if sortedEvents[i].time.minute < sortedEvents[j].time.minute {
				t := sortedEvents[i]
				sortedEvents[i] = sortedEvents[j]
				sortedEvents[j] = t
			}
		}
	}

	return sortedEvents
}

func main() {
	recordedEvents, guardSleepMap := parseInput("4.in")
	mostSleepGuardID := -1
	mostSleptMin := 0
	sleepMinutes := make(map[int]map[int]int)

	for _, g := range recordedEvents {
		currentGuard := g.id
		isSleep := false
		sleptMin := -1
		for _, v := range g.events {
			if v.action == begins {
				continue
			}
			if v.action == asleep {
				isSleep = true
				sleptMin = v.time.minute
			} else {
				if isSleep {
					isSleep = false
					guardSleepMap[currentGuard] += (v.time.minute - sleptMin)
					t := sleptMin
					if _, ok := sleepMinutes[currentGuard]; !ok {
						sleepMinutes[currentGuard] = make(map[int]int)
					}
					for t < v.time.minute {
						if _, ok := sleepMinutes[currentGuard][t]; !ok {
							sleepMinutes[currentGuard][t] = 1
						} else {
							sleepMinutes[currentGuard][t]++
						}
						t++
					}
					sleptMin = -1
				}
			}
		}
	}

	mostSleepTime := -1
	for k, v := range guardSleepMap {
		if v > mostSleepTime {
			mostSleepGuardID = k
			mostSleepTime = v
		}
	}

	mostSleepGuardMinutes := sleepMinutes[mostSleepGuardID]
	mostTimes := -1
	for k, v := range mostSleepGuardMinutes {
		if v > mostTimes {
			mostSleptMin = k
			mostTimes = v
		}
	}
	// part 1
	fmt.Println(mostSleepGuardID * mostSleptMin)

	mGuardID := -1
	mGuardMinute := -1
	mTimes := -1
	for k, v := range sleepMinutes {
		if k == -1 {
			continue
		}
		for min, times := range v {
			if times > mTimes {
				mTimes = times
				mGuardID = k
				mGuardMinute = min
			}
		}
	}

	// part 2
	fmt.Println(mGuardID * mGuardMinute)
}
