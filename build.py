from pybtex.database.input import bibtex

def get_personal_data():
    name = ["Jianfeng", "Li"]  # 修改为你的名字
    chinese_name = "李剑峰"  # 中文名字
    email = "popqlee@sina.com"
    twitter = ""  # 如果没有，可以留空
    github = ""  # 如果有GitHub用户名可以填写
    linkedin = ""  # 如果没有，可以留空

    bio_text = f"""
                <p>
                    <a href=\"https://ceie.swu.edu.cn/info/1116/4039.htm\" target=\"_blank\">Jianfeng Li</a>
                    is a Lecturer at Southwest University.
                    He received his Ph.D. from Hiroshima City University, advised by Prof.
                    <a href=\"https://hcur1.acoffice.biz/hcuhp/KgApp/k03/resid/S001766;jsessionid=39373EF817415A83B0E8C5A4B0B474E7?lang=en\" target=\"_blank\">Shigang Li</a>,
                    and his MPhil degree from Sichuan University, advised by Prof.
                    <a href=\"https://cs.scu.edu.cn/info/1073/3874.htm\" target=\"_blank\">Yiguang Liu</a>.
                </p>

                <div style=\"background: #fafafa; border-left: 3px solid #e6e6e6; padding: 10px 12px; margin: 10px 0;\">
                    <div style=\"font-weight: 600; margin-bottom: 6px;\">Research interests</div>
                    <ul style=\"margin-bottom: 0.35rem; padding-left: 1.2rem;\">
                        <li style=\"margin-bottom: 0.2rem;\">Panoramic images and omnidirectional images (360° vision)</li>
                        <li style=\"margin-bottom: 0.2rem;\">Representation and geometric understanding on spherical domains</li>
                        <li style=\"margin-bottom: 0.0rem;\">Facial expression understanding</li>
                    </ul>
                    <div style=\"color: #7A1E1E; font-size: 0.95em;\">Students interested in these topics are welcome to contact me.</div>
                </div>

                <p style=\"margin-bottom: 0;\">
                    <a href=\"mailto:{email}\" style=\"margin-right: 12px\">
                        <i class=\"far fa-envelope-open fa-lg\"></i> Email
                    </a>
                    <a href=\"https://scholar.google.com/citations?hl=zh-CN&user=iJDD27gAAAAJ&view_op=list_works&sortby=pubdate\" target=\"_blank\" style=\"margin-right: 12px\">
                        <i class=\"fa fa-graduation-cap fa-lg\"></i> Google Scholar
                    </a>
                    <a href=\"https://www.researchgate.net/profile/Jianfeng-Li-32\" target=\"_blank\" style=\"margin-right: 12px\">
                        <i class=\"fa-brands fa-researchgate fa-lg\"></i> ResearchGate
                    </a>
                </p>
    """

    footer = "<p>© 2026 Jianfeng Li. All rights reserved.</p>"
    return name, bio_text, footer

def get_author_dict():
    return {
        'Andreas Geiger': 'https://www.cvlibs.net/',
        'Songyou Peng': 'https://pengsongyou.github.io/',
        'Zehao Yu': 'https://niujinshuchong.github.io/',
        'Torsten Sattler': 'https://tsattler.github.io/',
        'Katja Schwarz': 'https://katjaschwarz.github.io/',
        'Axel Sauer': 'https://axelsauer.com/',
        'Jonathan Barron': 'https://jonbarron.info/',
        'Ben Mildenhall': 'https://bmild.github.io/',
        'Mehdi Sajjadi': 'https://msajjadi.com/',
        'Noha Radwan': 'http://www2.informatik.uni-freiburg.de/~radwann/',
        'Chiyu Jiang': 'https://www.maxjiang.ml/',
        'Yiyi Liao': 'https://yiyiliao.github.io/',
        'Marc Pollefeys': 'https://people.inf.ethz.ch/pomarc/',
        'Michael Oechsle': 'https://moechsle.github.io/',
        'Christian Reiser': 'https://creiser.github.io/',
        'Lars Mescheder': 'https://scholar.google.de/citations?user=h2k1gL4AAAAJ&hl=de',
        'Thilo Strauss': 'https://scholar.google.com/citations?user=VlymtLQAAAAJ&hl=en',
        'Sebastian Nowozin': 'http://www.nowozin.net/sebastian/',
        'Marie-Julie Rakotosaona': 'http://www.lix.polytechnique.fr/Labo/Marie-Julie.RAKOTOSAONA/',
        'Fabian Manhardt': 'https://campar.in.tum.de/Main/FabianManhardt',
        'Diego Martin Arroyo': 'https://martinarroyo.net/',
        'Abhijit Kundu': 'https://abhijitkundu.info/',
        'Federico Tombari': 'https://www.cs.cit.tum.de/camp/members/senior-research-scientists/federico-tombari/',
        'Anpei Chen': 'https://apchenstu.github.io/',
        'Bozidar Antic': 'https://bozidarantic.com/',
        'Apratim Bhattacharyya': 'https://apratimbhattacharyya18.github.io/',
        'Siyu Tang': 'https://inf.ethz.ch/people/person-detail.MjYyNzgw.TGlzdC8zMDQsLTg3NDc3NjI0MQ==.html',
        'Hidenobu Matsuki': 'https://dblp.org/pid/225/4487.html',
        'Keisuke Tateno': 'https://campar.in.tum.de/Main/KeisukeTateno',
        'Alessio Tonioni': 'https://alessiotonioni.github.io/',
        'Christina Tsalicoglou': 'https://scholar.google.ch/citations?user=7D10QQkAAAAJ&hl=en', 
        'Amit Raj': 'https://amitraj93.github.io/',
        'Srinivas Kaza': 'https://www.linkedin.com/in/srinivas-kaza-64223b74',
        'Ben Poole': 'https://poolio.github.io/',
        'Nataniel Ruiz': 'https://natanielruiz.github.io/',
        'Shiran Zada': 'https://scholar.google.com/citations?user=I2qheksAAAAJ',
        'Kfir Aberman': 'https://kfiraberman.github.io/',
        'Michael Rubinstein': 'http://people.csail.mit.edu/mrub/',
        'Yuanzhen Li': 'http://people.csail.mit.edu/yzli/',
        'Varun Jampani': 'https://varunjampani.github.io/',
        'Francis Engelmann': 'https://francisengelmann.github.io/',
        'Mohamad Shahbazi': 'https://mohamad-shahbazi.github.io/',
        'Liesbeth Claessens': 'https://asl.ethz.ch/the-lab/people/person-detail.MjY5NDUz.TGlzdC8xNTg0LDEyMDExMzk5Mjg=.html',
        'Edo Collins': 'https://www.linkedin.com/in/edo-collins/?originalSubdomain=ch',
        'Luc Van Gool': 'https://ee.ethz.ch/the-department/faculty/professors/person-detail.OTAyMzM=.TGlzdC80MTEsMTA1ODA0MjU5.html',
        'Fangjinhua Wang': 'https://fangjinhuawang.github.io/',
        'Richard Szeliski': 'https://szeliski.org/',
        'Kunyi Li': 'https://campus.tum.de/tumonline/ee/ui/ca2/app/desktop/#/pl/ui/$ctx/visitenkarte.show_vcard?$ctx=design=ca2;header=max;lang=de&pPersonenGruppe=3&pPersonenId=6EC78DAA25310FF2',
        'Nassir Navab': 'https://www.professoren.tum.de/en/navab-nassir',
        'Rama Gosula': 'https://arvr.google.com/',
        'John Bates': 'https://arvr.google.com/',
        'Dominik Kaeser': 'https://scholar.google.com/citations?user=DQ4838YAAAAJ&hl=en',
        'Erik Sandström': 'https://scholar.google.com/citations?user=phiETm4AAAAJ&hl=en',
        'Luc Van-Gool': 'https://insait.ai/prof-luc-van-gool/',
        'Martin Oswald': 'https://oswaldm.github.io/',
        'Fangneng Zhan': 'https://fnzhan.com/',
        'Hanxue Liang': 'https://scholar.google.com/citations?user=XcxDA14AAAAJ&hl=en',
        'Yifan Wang': 'https://yifita.netlify.app/',
        'Adam Kortylewski': 'https://genintel.mpi-inf.mpg.de/',
        'Cengiz Oztireli': 'https://www.cl.cam.ac.uk/~aco41/',
        'Gordon Wetzstein': 'https://stanford.edu/~gordonwz/', 
        'Christian Theobalt': 'https://people.mpi-inf.mpg.de/~theobalt/',
        'Siyun Liang': 'https://siyun-liang.github.io/',
        'Thomas Wimmer': 'https://wimmerth.github.io/',
        'Sen Wang': 'https://scholar.google.com/citations?user=OxZ9S6oAAAAJ&hl=en',
        'Stefano Gasperini': 'https://www.cs.cit.tum.de/camp/members/stefano-gasperini/',
        'Zeyu Chen': 'https://zeyuuuchen.github.io/',
        'Jonas Kulhanek': 'https://jkulhanek.com/',
        'Yiming Wang': 'https://scholar.google.com/citations?user=AVOZmU8AAAAJ&hl=en',
        'Lucy Chai': 'https://scholar.google.com/citations?user=bunnQWQAAAAJ&hl=en',
        'Xuan Luo': 'https://roxanneluo.github.io/',
        'Manuel Lagunas': 'https://mlagunas.me/',
        'Stephen Lombardi': 'https://stephenlombardi.github.io/',
        'Tiancheng Sun': 'https://www.kevinkingo.com/',
        'Tianshi Cao': 'https://scholar.google.com/citations?user=CZ9wBBoAAAAJ&hl=en',
        'Elena Alegret': 'https://es.linkedin.com/in/elena-alegret',
        'Maria Parelli': 'https://mparelli.github.io/',
        'Atakan Topaloglu': 'https://scholar.google.com/citations?user=l9mFndIAAAAJ&hl=en',
        'Xin Kong': 'https://kxhit.github.io/',
        'Daniel Watson': 'https://scholar.google.com/citations?user=ve9A9rMAAAAJ&hl=en',
        'Yannick Strümpler': 'https://scholar.google.com/citations?user=6UwR6EUAAAAJ&hl=de',
        'Ahmed Tekalp': 'https://mysite.ku.edu.tr/mtekalp/',
        }

def generate_person_html(persons, connection=", ", make_bold=True, make_bold_name='Jianfeng Li', add_links=True):
    links = get_author_dict() if add_links else {}
    s = ""
    for p in persons:
        string_part_i = ""
        for name_part_i in p.get_part('first') + p.get_part('last'): 
            if string_part_i != "":
                string_part_i += " "
            string_part_i += name_part_i
        if string_part_i in links.keys():
            string_part_i = f'<a href="{links[string_part_i]}" target="_blank">{string_part_i}</a>'
        if make_bold and string_part_i == make_bold_name:
            string_part_i = f'<span style="font-weight: bold";>{make_bold_name}</span>'
        if p != persons[-1]:
            string_part_i += connection
        s += string_part_i
    return s

def get_paper_entry(entry_key, entry):
    s = """<div style="margin-bottom: 3em;"> <div class="row"><div class="col-sm-3">"""
    s += f"""<img src="{entry.fields['img']}" class="img-fluid img-thumbnail" alt="Project image">"""
    s += """</div><div class="col-sm-9">"""

    # Title (optional link)
    title_html = entry.fields.get('title', '')
    if 'html' in entry.fields:
        title_html = f"""<a href=\"{entry.fields['html']}\" target=\"_blank\">{entry.fields['title']}</a>"""

    # Optional note (e.g., Coming soon)
    note_html = ""
    if 'note' in entry.fields:
        note_html = f""" <span style=\"color: #777;\">({entry.fields['note']})</span>"""

    if 'award' in entry.fields.keys():
        s += f"""{title_html}{note_html} <span style="color: red;">({entry.fields['award']})</span><br>"""
    else:
        s += f"""{title_html}{note_html} <br>"""

    s += f"""{generate_person_html(entry.persons['author'])} <br>"""
    s += f"""<span style="font-style: italic;">{entry.fields['booktitle']}</span>, {entry.fields['year']} <br>"""

    artefacts = {'html': 'Project Page', 'pdf': 'Paper', 'supp': 'Supplemental', 'video': 'Video', 'poster': 'Poster', 'code': 'Code'}
    i = 0
    for (k, v) in artefacts.items():
        if k in entry.fields.keys():
            if i > 0:
                s += ' / '
            s += f"""<a href="{entry.fields[k]}" target="_blank">{v}</a>"""
            i += 1

    cite = "<pre><code>@InProceedings{" + f"{entry_key}, \n"
    cite += "\tauthor = {" + f"{generate_person_html(entry.persons['author'], make_bold=False, add_links=False, connection=' and ')}" + "}, \n"
    for entr in ['title', 'booktitle', 'year']:
        if entr in entry.fields:
            cite += f"\t{entr} = " + "{" + f"{entry.fields[entr]}" + "}, \n"
    cite += """}</pre></code>"""

    # BibTeX toggle in the same style as other artefact links
    if i > 0:
        s += ' / '
    s += f"""<button class=\"btn btn-link\" type=\"button\" data-toggle=\"collapse\" data-target=\"#collapse{entry_key}\"
            aria-expanded=\"false\" aria-controls=\"collapse{entry_key}\" style=\"padding: 0;\">BibTeX</button>"""
    s += f"""<div class=\"collapse\" id=\"collapse{entry_key}\"><div class=\"card card-body\" style=\"margin-top: 8px;\">{cite}</div></div>"""

    s += """ </div> </div> </div>"""
    return s

def get_publications_html():
    parser = bibtex.Parser()
    bib_data = parser.parse_file('publication_list.bib')
    keys = bib_data.entries.keys()
    s = ""
    for k in keys:
        s+= get_paper_entry(k, bib_data.entries[k])
    return s

def get_index_html():
    pub = get_publications_html()
    name, bio_text, footer = get_personal_data()

    # News: show first 4 items, collapse the rest
    news_html = """
        <h4>News</h4>
        <ul style=\"margin-bottom: 0.25rem; padding-left: 1.2rem;\">
            <li style=\"margin-bottom: 0.25rem;\"><span style=\"color:#666; display:inline-block; width:4.2em;\">2026.2</span> One paper accepted to CVPR 2026.</li>
            <li style=\"margin-bottom: 0.25rem;\"><span style=\"color:#666; display:inline-block; width:4.2em;\">2025.7</span> One paper accepted to ECAI 2025.</li>
            <li style=\"margin-bottom: 0.25rem;\"><span style=\"color:#666; display:inline-block; width:4.2em;\">2024.3</span> One paper accepted to ICRA 2024.</li>

            <div class=\"collapse\" id=\"newsMore\">
            <li style=\"margin-bottom: 0.25rem;\"><span style=\"color:#666; display:inline-block; width:4.2em;\">2024.1</span> One paper accepted to WACV 2024.</li>
            <li style=\"margin-bottom: 0.25rem;\"><span style=\"color:#666; display:inline-block; width:4.2em;\">2022.7</span> One paper accepted to ISMAR 2022.</li>
                
            </div>
        </ul>

        <button id=\"newsToggleBtn\" class=\"btn btn-link\" type=\"button\" data-toggle=\"collapse\" data-target=\"#newsMore\" aria-expanded=\"false\" aria-controls=\"newsMore\" style=\"padding: 0;\">More...</button>
        <script>
          (function() {
            var more = document.getElementById('newsMore');
            var btn = document.getElementById('newsToggleBtn');
            if (!more || !btn) return;
            more.addEventListener('show.bs.collapse', function () { btn.textContent = 'Less'; });
            more.addEventListener('hide.bs.collapse', function () { btn.textContent = 'More...'; });
          })();
        </script>
    """

    mentoring_html = """
        <h4>Mentoring</h4>
        <p style=\"margin-bottom: 0.4rem; color: #555;\">I feel very fortunate to have worked with these talented students.</p>
        <ul style=\"margin-bottom: 0.25rem; padding-left: 1.2rem;\">
            <li style=\"margin-bottom: 0.25rem;\"><span style=\"color:#666; font-weight:600; display:inline-block; width:4.2em;\">MPhil</span> <b>Yaqi Song</b> → Xiaomi Inc.</li>
            <li style=\"margin-bottom: 0.25rem;\"><span style=\"color:#666; font-weight:600; display:inline-block; width:4.2em;\">MPhil</span> <b>Jingguo Liu</b> → KE Holdings Inc.</li>
            <li style=\"margin-bottom: 0.25rem;\"><span style=\"color:#666; font-weight:600; display:inline-block; width:4.2em;\">MPhil</span> <b>Lin Lei</b> → Sichuan University (PhD)</li>
            <li style=\"margin-bottom: 0.25rem;\"><span style=\"color:#666; font-weight:600; display:inline-block; width:4.2em;\">UG</span> <b>Junjie Liu</b> → South China University of Technology (MPhil) → SUSTech (PhD)</li>
            <li style=\"margin-bottom: 0.0rem;\"><span style=\"color:#666; font-weight:600; display:inline-block; width:4.2em;\">UG</span> <a href=\"https://zhongleilz.github.io/\" target=\"_blank\"><b>Lei Zhong</b></a> → Nankai University (MPhil) → University of Edinburgh (PhD)</li>
        </ul>
    """

    s = f"""
    <!doctype html>
<html lang=\"en\">

<head>
  <!-- Required meta tags -->
  <meta charset=\"utf-8\">
  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1, shrink-to-fit=no\">

  <!-- Bootstrap CSS -->
  <link rel=\"stylesheet\" href=\"https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css\"
    integrity=\"sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm\" crossorigin=\"anonymous\">
    <link rel=\"stylesheet\" href=\"https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.2.0/css/all.min.css\" integrity=\"sha512-xh6O/CkQoPOWDdYTDqeRdPCVd1SpvCA9XXcUnZS2FmJNp1coAFzvtCN9BmamE+4aHK8yyUHUSCcJHgXloTyT2A==\" crossorigin=\"anonymous\" referrerpolicy=\"no-referrer\" />

  <title>{name[0] + ' ' + name[1]}</title>
  <link rel=\"icon\" type=\"image/x-icon\" href=\"assets/favicon.ico\">
</head>

<body>
    <div class=\"container\">
        <div class=\"row\">
            <div class=\"col-md-1\"></div>
            <div class=\"col-md-10\">
                <div class=\"row\" style=\"margin-top: 3em;\">
                    <div class=\"col-sm-12\" style=\"margin-bottom: 1em;\">
                    <h3 class=\"display-4\" style=\"text-align: center;\"><span style=\"font-weight: bold;\">{name[0]}</span> {name[1]}</h3>
                    </div>
                    <br>
                    <div class=\"col-md-10\" style=\"\">
                        {bio_text}
                    </div>
                    <div class=\"col-md-2\" style=\"\">
                        <img src=\"assets/img/profile.jpg\" class=\"img-thumbnail\" width=\"280px\" alt=\"Profile picture\">
                    </div>
                </div>

                <div class=\"row\" style=\"margin-top: 1.99em;\">
                    <div class=\"col-sm-12\">
                        {news_html}
                    </div>
                </div>

                <div class=\"row\" style=\"margin-top: 1.99em;\">
                    <div class=\"col-sm-12\">
                        {mentoring_html}
                    </div>
                </div>

                <div class=\"row\" style=\"margin-top: 1.99em;\">
                    <div class=\"col-sm-12\" style=\"\">
                        <h4>
                            Selected Publications
                            <a href="https://scholar.google.com/citations?hl=zh-CN&user=iJDD27gAAAAJ&view_op=list_works&sortby=pubdate" target="_blank" style="font-weight: normal; font-size: 0.9em; margin-left: 8px;">(Full Papers)</a>
                        </h4>
                        {pub}
                    </div>
                </div>
                <div class=\"row\" style=\"margin-top: 3em; margin-bottom: 1em;\">
                    {footer}
                </div>
            </div>
            <div class=\"col-md-1\"></div>
        </div>
    </div>

    <!-- Optional JavaScript -->
    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    <script src=\"https://code.jquery.com/jquery-3.2.1.slim.min.js\"
      integrity=\"sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN\"
      crossorigin=\"anonymous\"></script>
    <script src=\"https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js\"
      integrity=\"sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q\"
      crossorigin=\"anonymous\"></script>
    <script src=\"https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js\"
      integrity=\"sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl\"
      crossorigin=\"anonymous\"></script>
</body>

</html>
    """
    return s


def write_index_html(filename='index.html'):
    s = get_index_html()
    with open(filename, 'w') as f:
        f.write(s)
    print(f'Written index content to {filename}.')

if __name__ == '__main__':
    write_index_html('index.html')
