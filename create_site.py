from elements import *

page = Page([
    Row("logo", "#ffffff", {
        "filename": "intro_sub_anim.gif"
    }),
    NavBar({
        "soundcloud": {"address": "https://soundcloud.com/mitanimationgroup", "color": "#FE4800"},
        "facebook": {"address": "http://www.facebook.com/mitanimationgroup", "color": "#3B579D"},
        "vimeo": {"address": "https://vimeo.com/mitag", "color": "#2a89a9"},
        "email": {"address": "mailto: mitag_exec@mit.edu", "color": "#CEB182"}
    }),
    Section(
        "",
        "",
        "nav",
        "#000000",
        "#303030",
        [
            {
                "type": "links",
                "name": "",
                "links": [{"name": "About Us", "address": "#about"}, {"name": "Films", "address": "#films"}, {"name": "Events", "address": "#events"}, {"name": "Schedule", "address": "#schedule"}, {"name": "Join", "address": "#join"}]
            },
        ]
    ),
    Section(
        "About Us",
        "MITAG membership, sponsors, and mission",
        "about",
        "#606060",
        "#464646",
        [
            {
                "type": "text",
                "name": "Mission:",
                "text": "The primary goal of the MIT Animation Group is to provide an environment where MIT students can both express their creativity through an art form of their choice and collaborate with other artists who specialize in different art forms.<br><br>In addition, the MIT Animation Group is intended to expose students to the art of animation and film production, and to let students learn about these arts from their peers and industry experts."
            },
            {
                "type": "people",
                "name": "Executive Team:",
                "people": [
                    {
                        "name": "Joanna Gerr - President",
                        "filename": "joanna.png"
                    },
                    {
                        "name": "Marwa Al Alawi - Treasurer",
                        "filename": "marwa.png"
                    },
                    {
                        "name": "Caleb Richardson - Audio Director",
                        "filename": "caleb.png"
                    },
                    {
                        "name": "Heya Lee - Marketing Director",
                        "filename": "heya.png"
                    },
                    {
                        "name": "Karen Gao - Animation Director",
                        "filename": "karen.png"
                    }
                ],
            },
            {
                "type": "people",
                "name": "Sponsors:",
                "people": [
                    {
                        "name": "Council for the Arts at MIT",
                        "filename": "camitlogo.png"
                    },
                    {
                        "name": "MIT Undergraduate Association",
                        "filename": "ualogo.png"
                    },
                ],
            },
        ]
    ),
    Section(
        "Films",
        "MITAG-related student film projects",
        "films",
        "#383838",
        "#555555",
        [
            {
                "type": "video-vimeo",
                "name": "Lily Pads & Pebbles:",
                "address": "https://player.vimeo.com/video/285221890",
            },
            {
                "type": "video-vimeo",
                "name": "backspace:",
                "address": "https://player.vimeo.com/video/285221980",
            },
            {
                "type": "video-vimeo",
                "name": "An Extra Dimension:",
                "address": "https://player.vimeo.com/video/242282080",
            },
        ]
    ),
    Section(
        "Events",
        "Past events including workshops & classes",
        "events",
        "#606060",
        "#464646",
        [
            {
                "type": "img_gallery",
                "name": "CPW Character Design Workshop - Apr. 2019:",
                "extension": "cpwworkshop",
                "multipliers": [1.25, 1, 1.25, 1.25]
            },
            {
                "type": "img_gallery",
                "name": "HackMIT - How to Use 3D Models and AR in iOS - Sept. 2018:",
                "extension": "hackmitar",
                "multipliers": []
            },
            {
                "type": "img_gallery",
                "name": "6.S087 - Learn to Animate with Stop-Motion (Class) - Jan. 2018:",
                "extension": "6s087",
                "multipliers": []
            },
            {
                "type": "img_gallery",
                "name": "Michael Scaramozzino - Creating 3D Animated Shorts - 11/19/17:",
                "extension": "mscara",
                "multipliers": []
            },
            {
                "type": "text",
                "name": "Other Events (Not Pictured Above):",
                "text": '''
                    Thought Cafe Animation Crash Course<br><br>
                    aniMIThon Short Film Competition (Spring 2018)<br><br>
                    MIT Animation Group & MIT Anime Club Joint Study Break<br><br>
                    Spark 2018 Claymation Tutorial<br><br>
                    Manga with Marwa (Character Design and Illustration Workshop)<br><br>
                    Flipbook & Character Design Workshop<br><br>
                    ...and many others!
                '''
            },
        ]
    ),
    Section(
        "Schedule",
        "Calendar of upcoming MITAG events",
        "schedule",
        "#383838",
        "#555555",
        [
            {
                "type": "custom",
                "name": "Tentative Upcoming Events Schedule:",
                "size": "big",
                "snippet": '''
                    <iframe src="https://calendar.google.com/calendar/embed?src=otulkg74i6kr4t7f8knb7s9t28%40group.calendar.google.com&ctz=America%2FNew_York" style="border: 0" width="90%" height="370" frameborder="0" scrolling="no"></iframe>
                ''',
            },
        ]
    ),
    Section(
        "Join",
        "Information for joining MITAG",
        "join",
        "#606060",
        "#464646",
        [
            {
                "type": "links",
                "name": "Relevant Links:",
                "links": [{"name": "Exec Team Interest Form", "address": "https://docs.google.com/forms/d/e/1FAIpQLSd483MZ3iNu3ztmI8F0sv6Xv6E2ze1odD6wGqgGNno2KPUDjA/viewform?usp=sf_link"}, {"name": "Mailing List Signup Form", "address": "https://docs.google.com/forms/d/e/1FAIpQLSdSeO8985It-pmbNk9PkoY4AznYIH9eh8FXNRXLKkS_okgWNg/viewform?usp=sf_link"}]
            },
        ]
    ),
], "index.html")
page.write()