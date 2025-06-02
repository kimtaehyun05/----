import requests
import webbrowser
from googletrans import Translator

# API 키 설정
TMDB_API_KEY = 'cba511a5cd8d9c9fdb4d7297c1e555bd'
UNOGS_API_KEY = 'e232918b50msh15dc890c9e18b2fp181942jsn078e62dc0b4b'
UNOGS_HOST = 'unogsng.p.rapidapi.com'

# 번역기 초기화
translator = Translator()

# TMDB 장르 목록 조회
def get_tmdb_genres():
    url = f"https://api.themoviedb.org/3/genre/movie/list"
    params = {'api_key': TMDB_API_KEY, 'language': 'ko-KR'}
    response = requests.get(url, params=params)
    genres = response.json().get('genres', [])
    return {g['name']: g['id'] for g in genres}

# TMDB 인기 영화 + 장르 필터
def fetch_tmdb_movies_by_genre(selected_genre_id):
    url = "https://api.themoviedb.org/3/movie/popular"
    params = {'api_key': TMDB_API_KEY, 'language': 'ko-KR'}
    response = requests.get(url, params=params)
    results = response.json().get("results", [])
    if selected_genre_id:
        results = [m for m in results if selected_genre_id in m.get('genre_ids', [])]
    return results

# uNoGS 장르 샘플 (정적, uNoGS는 장르 ID 미제공)
UNOGS_GENRES = [
    'action', 'adventure', 'animation', 'comedy', 'crime',
    'documentary', 'drama', 'family', 'fantasy', 'horror',
    'romance', 'sci-fi', 'thriller', 'war'
]

# uNoGS 넷플릭스 콘텐츠 추천 (한국 넷플릭스에서 볼 수 있는 콘텐츠만)
def fetch_unogs_recommendations(genre, year, limit=10): # country_filter 파라미터 제거
    url = f"https://{UNOGS_HOST}/search"
    headers = {
        "X-RapidAPI-Key": UNOGS_API_KEY,
        "X-RapidAPI-Host": UNOGS_HOST
    }
    params = {
        "query": genre,
        "start_year": year,
        "countrylist": "78",  # 항상 한국 넷플릭스 (국가 ID 78)로 고정
        "limit": 50  # 넉넉히 받아서 연도 필터링
    }
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status() # HTTP 에러 발생 시 예외 발생

    all_results = response.json().get("results", [])

    # 연도 필터
    final_results = [item for item in all_results if item.get('year') and int(item['year']) >= year]

    # 더 이상 제목의 한글 여부로 국적을 구분하지 않음
    # 모든 결과는 한국 넷플릭스에서 시청 가능한 콘텐츠로 간주

    return final_results[:limit]


# 결과 출력
def display_tmdb_results(movies):
    if not movies:
        print("❌ 해당 장르의 추천 영화가 없습니다.")
        return
    for m in movies:
        print(f"\n🎬 제목: {m.get('title')}")
        print(f"📅 개봉일: {m.get('release_date')}")
        print(f"📝 개요: {m.get('overview') or '내용 없음'}")
        print("-" * 60)

def display_unogs_results(results):
    if not results:
        print("❌ 추천 결과가 없습니다. 조건을 다시 확인해 보세요.")
        return
    for item in results:
        title = item.get('title')
        year = item.get('year')
        synopsis = item.get('synopsis', '')
        # synopsis가 비어있거나 번역이 필요 없는 경우를 처리
        translated = translator.translate(synopsis, dest='ko').text if synopsis else '내용 없음'

        # 이제는 모든 콘텐츠가 한국 넷플릭스 기준이므로 국적 표기는 일반화
        print(f"\n🎬 제목: {title} ({year})")
        print(f"📝 개요: {translated}")
        print("-" * 60)


# 메인 함수
def main():
    print("🎥 영화/OTT 콘텐츠 탐색기")
    print("1. 인기 영화 보기 (TMDB)")
    print("2. 넷플릭스 추천 보기 (uNoGS)")

    choice = input("번호를 선택하세요 (1 또는 2): ").strip()

    if choice == '1':
        genres = get_tmdb_genres()
        print("\n[🎞 장르 목록]")
        for g in genres:
            print(f"- {g}")
        selected = input("추천을 원하는 장르를 입력하세요 (예: 액션): ").strip()
        genre_id = genres.get(selected)
        movies = fetch_tmdb_movies_by_genre(genre_id)
        display_tmdb_results(movies)

        print("\n👉 더 많은 정보를 보시려면 CGV 홈페이지를 방문하세요: https://www.cgv.co.kr/movies/")
        if input("CGV 홈페이지를 열까요? (y/n): ").strip().lower() == 'y':
            webbrowser.open("https://www.cgv.co.kr/movies/")

    elif choice == '2':
        print("\n[📺 장르 목록 (영문 입력)]")
        print(", ".join(UNOGS_GENRES))
        genre = input("장르 입력 (예: comedy): ").strip().lower()
        year = input("몇 년 이후 콘텐츠를 추천받고 싶으신가요? (예: 2020): ").strip()
        year = int(year) if year.isdigit() else 2020

        # country_filter 입력 제거
        print("\n⭐ 한국 넷플릭스에서 시청 가능한 콘텐츠를 추천합니다.")
        results = fetch_unogs_recommendations(genre, year) # country_filter 인자 제거
        display_unogs_results(results)

    else:
        print("⚠️ 잘못된 입력입니다.")

if __name__ == '__main__':
    main()