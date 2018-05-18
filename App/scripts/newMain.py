def main():
        global driver
        global username
        global password

        input = '{"event_contact_name":"1","event_contact_number":"1111111111","event_organizer_name":"1","event_organizer_email":"1@1","event_organizer_phone_number":"1111111111","event_title":"1","event_date_start":"August 7, 2018 9:35 AM","event_date_end":"August 29, 2018 5:35 PM","event_url":"1","event_age_group":"1","event_price":"1","event_ticket_url":"1","event_details":"1","event_venue":"1","event_street":"1","event_city":"1","event_postal_code":"1","event_websites":["Test"]}'
        info = json.loads(input)

        functions = {
                "Eventful": eventful,
                "Youth Core": youthCore,
                "Planet Friendly":planetFriendly,
                "Global News": globalNews,
                "Kijiji": kijiji,
                "Metro Vancouver": metroVancouver,
                "Community of North Vancouver": cnv,
                "Ubyssey": ubyssey,
                "North Shore": northShore,
                "Craigslist": craigsList,
                "Test":test
                }

        for website in info['event_websites']:
            try:
                functions[website](info)
            except Exception:
                pass

        print(websites)
        sys.stdout.flush()