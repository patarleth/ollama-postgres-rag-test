import ICAL from 'ical.js';
import fs from 'fs';

const icalStr = fs.readFileSync('/Users/patarleth/projects/ollama_tests/demo/weha-meetings-all-public.ical').toString()

// Fetch the iCal file (e.g., using fetch API)
const jcal = ICAL.parse(icalStr);
const vcal = new ICAL.Component(jcal)
const events = vcal.getAllSubcomponents('vevent')

const dateFormatter = new Intl.DateTimeFormat('en-US', { dateStyle: 'full' });
const timeFormatter = new Intl.DateTimeFormat('en-US', { timeStyle: 'short' });


const regex = / [mM]eeting/gi;

let messageDict = {}

for (const event of events) {
    let summary = event.getFirstPropertyValue('summary');
    summary = summary.trim().replaceAll(regex, '')
    
    const location = event.getFirstPropertyValue('location');
    let description = event.getFirstPropertyValue('description');
    description = description ? description.trim() : ''
    if( description != '' ) {
	description = ' - ' + description
    }
    const start = event.getFirstPropertyValue('dtstart')
    const end = event.getFirstPropertyValue('dtend')

    const startDate = start ? start.toJSDate() : null
    const endDate = end ? end.toJSDate() : startDate

    const formattedDate = dateFormatter.format(startDate).replaceAll(',','');
    const formattedTime = timeFormatter.format(startDate);

    const meetingMsg = `On ${formattedDate} at ${formattedTime}, the town of West Hartford in CT is holding a meeting for the ${summary}, held at ${location}${description}.`


    const monthName = startDate.toLocaleString('default', { month: 'long' });
    const mYrKey = monthName + ' ' + startDate.getFullYear()

    let messageData = {}
    if (messageDict[mYrKey]) {
	messageData = messageDict[mYrKey]
    } else {
	messageDict[mYrKey] = { 'title': `${monthName} ${startDate.getFullYear()} Meetings in West Hartford`, 'content': meetingMsg }
    }

    messageDict[mYrKey].content = messageDict[mYrKey].content + '\n' + meetingMsg
}

let dataArray = new Array()

Object.keys(messageDict).forEach(key => {
    const next = messageDict[key]
    dataArray.push( { 'title': next.title, 'content': next.content } )
})

console.log(JSON.stringify(dataArray, null, 2))
