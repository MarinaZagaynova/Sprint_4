import pytest

from main import BooksCollector


class TestBooksCollector:

    @pytest.fixture()
    def collector(self):
        collector = BooksCollector()
        return collector

    def test_add_new_book_add_two_books(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        assert len(collector.get_books_genre()) == 2

    def test_add_new_book_add_one_book(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        assert len(collector.get_books_genre()) == 1

    @pytest.mark.parametrize('name, genre', [['Гордость и предубеждение и зомби', 'Фантастика'],
                                             ['Что делать, если ваш кот хочет вас убить', 'Ужасы']])
    def test_set_book_genre_add_two_genre(self, name, genre, collector):
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.books_genre[name] == genre

    def test_set_book_genre_add_no_genre(self, collector):
        collector.add_new_book('Что делать')
        collector.set_book_genre('Что делать', 'genre')
        assert collector.books_genre['Что делать'] == ""

    @pytest.mark.parametrize('name, genre', [['Гордость и предубеждение и зомби', 'Фантастика'],
                                             ['Что делать, если ваш кот хочет вас убить', 'Ужасы']])
    def test_get_book_genre_two_genre(self, name, genre, collector):
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.get_book_genre(name) == genre

    def test_get_books_with_specific_genre_for_two_genre(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби 1')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить 1')
        collector.add_new_book('Гордость и предубеждение и зомби 2')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить 2')
        collector.set_book_genre('Гордость и предубеждение и зомби 1', 'Фантастика')
        collector.set_book_genre('Гордость и предубеждение и зомби 2', 'Фантастика')
        collector.set_book_genre('Что делать, если ваш кот хочет вас убить 1', 'Ужасы')
        collector.set_book_genre('Что делать, если ваш кот хочет вас убить 2', 'Ужасы')
        assert collector.get_books_with_specific_genre('Фантастика') == ['Гордость и предубеждение и зомби 1',
                                                                         'Гордость и предубеждение и зомби 2']

    def test_get_books_genre(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Фантастика')
        collector.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Ужасы')
        assert len(collector.get_books_genre()) == 2

    def test_get_books_for_children_from_two_books(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Фантастика')
        collector.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Ужасы')
        assert len(
            collector.get_books_for_children()) == 1 and collector.get_books_for_children() == [
                   'Гордость и предубеждение и зомби']

    def test_add_book_in_favorites_one_book_from_two_books(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Фантастика')
        collector.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Ужасы')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        assert collector.favorites == ['Гордость и предубеждение и зомби'] and len(collector.favorites) == 1

    def test_delete_book_from_favorites_one_book_from_two_books(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Фантастика')
        collector.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Ужасы')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Что делать, если ваш кот хочет вас убить')
        collector.delete_book_from_favorites('Гордость и предубеждение и зомби')
        assert collector.favorites == ['Что делать, если ваш кот хочет вас убить'] and len(collector.favorites) == 1

    def test_get_list_of_favorites_books_two_books(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Фантастика')
        collector.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Ужасы')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Что делать, если ваш кот хочет вас убить')
        assert collector.get_list_of_favorites_books() == ['Гордость и предубеждение и зомби',
                                                           'Что делать, если ваш кот хочет вас убить'] and len(
            collector.favorites) == 2
