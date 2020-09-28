import styled from 'styled-components';

export const Container = styled.div`
  height: 40vh;
  width: 100%;
  background: rgba(50,50,50,0.4);
  color:#8FBB;
`;

export const Content = styled.div`
  width: 100%;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  padding: 0.5rem 1.5rem;

  header {
    font-size: 18px;
    font-weight: 600;
    text-align: center;
    padding-bottom: 0.5rem;
    margin-bottom:16px;
    border-bottom:1px solid #8FBB;
    
  }
`;

export const Wrapper = styled.div`
  width: 100%;
  display: flex;
  justify-content: space-between;
  font-size: 14px;
`;

export const Title = styled.h2`
  text-transform: uppercase;
  margin-bottom: 0.825rem;
`;

export const Subtitle = styled.h4`
  text-transform: uppercase;
  margin-bottom: 0.825rem;
`;

export const List = styled.div``;

export const ListItem = styled.div`
  padding: 0.1rem;
`;
