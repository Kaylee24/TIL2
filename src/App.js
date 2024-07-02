import logo from './logo.svg';
import './App.css';
import { useState } from 'react';
import { isDisabled } from '@testing-library/user-event/dist/utils';

function App() {

  let post = '부산 돼지국밥 맛집';
  // document.querySelector('h4').innerHTML = post;
  let [title, setTitle] = useState(['남자 코트 추천', '부산 돼지국밥 맛집', '파이썬 독학']);
  // let [titleB, setTitleB] = useState('부산 돼지국밥 맛집');
  // let [titleC, setTitleC] = useState('파이썬 독학');
  let [liked, likedUpdate] = useState(0);

  return (
    <div className="App">
      <div className="black-nav">
        <h4>Blog</h4>
      </div>

      {/* <div className='list'>
        <h4>글제목</h4>
        <p>2월 17일 발행</p>
      </div> */}

      {/* <div className='list'>
        <h4>{ titleA }</h4>
        <p>2월 17일 발행</p>
      </div>

      <div className='list'>
        <h4>{ titleB }</h4>
        <p>2월 17일 발행</p>
      </div>

      <div className='list'>
        <h4>{ titleC }</h4>
        <p>2월 17일 발행</p>
      </div> */}

      <button onClick={()=>{
        let copy = [...title];
        copy[0] = '여자 코트 추천'
        setTitle(copy)
      }}>글수정 ♀♂
      </button>

      <div className='list'>
        {/* <h4>{ title[0] } <span>👍</span> 0 </h4> */}
        <h4>{ title[0] }
          <span onClick={()=>{ likedUpdate(liked+1) }}>👍</span> {liked} </h4>
        <p>2월 17일 발행</p>
      </div>

      <div className='list'>
        <h4>{ title[1] }</h4>
        <p>2월 17일 발행</p>
      </div>

      <div className='list'>
        <h4>{ title[2] }</h4>
        <p>2월 17일 발행</p>
      </div>


    <h4 style={ { color : 'blue', fontSize : '14px' } }>{ post }</h4>
    </div>
  );
}

export default App;
